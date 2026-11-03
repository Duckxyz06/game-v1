# Prompt for Claude Code

Bạn là Senior Game Technical Artist + Godot 4 Engineer + Skills Architect. Xây dựng dự án game khám phá Bảo tàng Đồng Tháp, học tiếng Anh lịch sử. Nguồn tham chiếu: https://github.com/clbsinhvien5totdthu/ENGLISHFARM và demo https://clbsinhvien5totdthu.github.io/ENGLISHFARM/ . Repo đích: https://github.com/Duckxyz06/game-v1.git .

1. Đọc .claude/skills/dong-thap-pixel-assets/SKILL.md, docs/ASSET_MANIFEST.csv, docs/REFERENCE_SOURCES.md, docs/CHATGPT_ASSET_PROMPT_TEMPLATE.md; đọc các tài liệu Word/HTML người dùng đính kèm.
2. Clone ENGLISHFARM read-only, chạy git ls-tree -r --name-only HEAD > docs/ENGLISHFARM_FULL_FILE_TREE.txt; kiểm tra README.md, game.js, assets.js, house_assets.js, ground_assets.js, data/characters.js và data/quest_data.js. Đây là web JS, KHÔNG phải game Godot.
3. Không sao chép asset bên thứ ba khi chưa chứng minh được giấy phép. Tạo prompt để ChatGPT sinh ảnh pixel GỐC, nhận file PNG, kiểm tra kích thước, transparency, perspective, đồng nhất nhân vật/hướng/chuyển động.
4. Từ manifest, xuất sprites nhân vật sinh viên Sư phạm Lịch sử ĐH Đồng Tháp, NPC Sen Hồng, museum guide, tòa bảo tàng, dinh cò, dinh quận, nhà thầy thuốc Lư, trại giam, cây cối, nền, hàng rào, MiG-17, UH-1, pháo, tàu, Vishnu I, Vishnu II, Lakshmi, hiện vật vàng Óc Eo, UI. Không bịa đặc điểm lịch sử.
5. Mỗi asset cần PNG RGBA, JSON metadata, nguồn, mức độ xác thực, collision, frame size, animation states. Bất kỳ ảnh chưa có thì trạng thái pending.
6. Nếu repo trống, khởi tạo project.godot và prototype Godot 4 scene player/NPC/map/dialogue, collision không xuyên hàng rào, Y-sort, CanvasLayer textbox và input, camera. Không viết API Godot 3.
7. Kiểm tra mọi file, ghi docs/FILE_INVENTORY.md và docs/ASSET_STATUS.md; viết validator Pillow; chạy test, chỉ báo thành công khi có tệp thật.
8. Dùng branch feat/pixel-asset-skill, push, mở PR vào main. Không force push; không xoá tài liệu cũ. Báo PR URL và số lượng asset thực sự.
