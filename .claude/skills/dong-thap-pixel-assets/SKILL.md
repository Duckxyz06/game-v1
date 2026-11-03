---
name: dong-thap-pixel-assets
description: Create and QA original top-down pixel characters, elements, tilesets and animation for Dong Thap Museum RPG with ChatGPT image generation and Godot 4 integration.
---
# Dong Thap Pixel Art Asset Skill

Roles: Claude builds specifications, image prompts, QA scripts, metadata and Godot integration; ChatGPT creates ORIGINAL images. Never claim PNGs exist without checking files. The reference ENGLISHFARM is a JavaScript web game, not a Godot project.

Standards: 32x32 map tiles; characters logical 32x48 per frame; 4 directions ordered down,left,right,up; walk 4 frames per direction; RGBA PNG and transparent background for objects/characters; pixel-perfect nearest-neighbor, no blur/anti-alias; no mixed perspective. Physical collision footprint separate from roofs/tree crowns.

Process: (1) inspect reports, photo identity and license (2) inspect docs/ASSET_MANIFEST.csv (3) build one asset brief for ChatGPT (4) generate actual PNG (5) validate dimensions/transparency/frame consistency and historical fidelity (6) save JSON metadata (7) integrate into Godot 4 AnimatedSprite2D or TileSet, CharacterBody2D collision, Y-sort, CanvasLayer dialogue (8) test and report pending assets. Never copy image assets from ENGLISHFARM without an explicit suitable license. National treasures Vishnu I, Vishnu II, Lakshmi are distinct.

Metadata fields: id,category,image_path,source_reference,source_license,historical_confidence,tile_size,frame_size,directions,animations,origin,collision,tags,prompt_version.

Use docs/CHATGPT_ASSET_PROMPT_TEMPLATE.md for prompt format; inspect source references in docs/REFERENCE_SOURCES.md. Honest QA: missing image == pending, not complete.
