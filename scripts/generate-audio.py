"""
Pre-generate Swedish TTS audio files for all kunskapskrav and examples.

Uses edge-tts (Microsoft neural voices):
  - sv-SE-SofieNeural (female)
  - sv-SE-MattiasNeural (male)

Output:
  public/audio/sofie/<hash>.mp3
  public/audio/mattias/<hash>.mp3
  src/data/audio-manifest.json  { text_hash: true }

The frontend reads audio-manifest.json and builds audio URLs:
  /audio/sofie/<hash>.mp3
  /audio/mattias/<hash>.mp3
"""

import asyncio
import hashlib
import json
import re
from pathlib import Path

import edge_tts

ROOT = Path(__file__).parent.parent
DATA = ROOT / "src" / "data"
AUDIO_ROOT = ROOT / "public" / "audio"
MANIFEST = DATA / "audio-manifest.json"

VOICES = {
    "sofie": "sv-SE-SofieNeural",
    "mattias": "sv-SE-MattiasNeural",
}


def text_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:12]


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"🔊", "", text)
    return re.sub(r"\s+", " ", text).strip()


def collect_texts() -> set[str]:
    texts: set[str] = set()

    for course in ["b", "c", "d"]:
        data = json.loads((DATA / f"kurs-{course}.json").read_text(encoding="utf-8"))
        for domain in data["domains"].values():
            for goal in domain["goals"]:
                t = goal["text"].strip()
                if t:
                    texts.add(t)

    examples = json.loads((DATA / "examples.json").read_text(encoding="utf-8"))
    for raw in examples.values():
        for part in raw.split("|"):
            clean = strip_html(part)
            if clean and len(clean) > 1:
                texts.add(clean)

    return texts


async def generate_one(text: str, voice_key: str, voice_id: str) -> tuple[str, bool]:
    h = text_hash(text)
    out = AUDIO_ROOT / voice_key / f"{h}.mp3"
    if out.exists() and out.stat().st_size > 0:
        return h, False
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        communicate = edge_tts.Communicate(text, voice_id)
        await communicate.save(str(out))
        return h, True
    except Exception as e:
        print(f"  ERROR on '{text[:40]}...': {e}")
        return h, False


async def main():
    texts = collect_texts()
    print(f"Collected {len(texts)} unique texts")

    manifest: dict[str, str] = {}
    for t in texts:
        manifest[text_hash(t)] = t

    tasks = []
    for t in texts:
        for voice_key, voice_id in VOICES.items():
            tasks.append(generate_one(t, voice_key, voice_id))

    print(f"Generating {len(tasks)} audio files...")

    SEM = asyncio.Semaphore(10)

    async def limited(coro):
        async with SEM:
            return await coro

    results = await asyncio.gather(*[limited(t) for t in tasks])
    new_count = sum(1 for _, created in results if created)
    skipped = len(results) - new_count
    print(f"Created: {new_count}, Skipped (cached): {skipped}")

    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote manifest: {MANIFEST}")


if __name__ == "__main__":
    asyncio.run(main())
