import os

# 파일 생성을 원하는 경로 (현재 폴더에 생성하려면 '.' 유지)
target_directory = "."

# 3월(03)부터 12월(12)까지 반복
for month in range(2, 3):
    # 01부터 11까지 반복
    for day in range(5, 12):
        # 파일명 형식 지정 (03-01.html 등)
        file_name = f"{month:02d}-{day:02d}.html"
        file_path = os.path.join(target_directory, file_name)
        
        # 빈 파일 생성
        with open(file_path, 'w', encoding='utf-8') as f:
            # 기본적인 HTML 구조를 넣고 싶다면 아래 주석을 해제하세요.
            # f.write(f"<!DOCTYPE html>\n<html>\n<head><title>{file_name}</title></head>\n<body></body>\n</html>")
            pass

print(f"총 {10 * 11}개의 파일 생성이 완료되었습니다.")