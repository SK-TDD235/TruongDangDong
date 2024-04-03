#Trương Đăng Đông
# Đề Bài : Đọc 1 file văn bản gồm nhiều dòng ghi ra màn hình thứ tự ngược lại theo các dòng

def main():
    file_name = 'debaitext.txt'

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        print("Các dòng theo thứ tự ngược lại:")
        for line in reversed(lines):
            print(line.strip()) 
    except FileNotFoundError:
        print(f"Tệp '{file_name}' không tồn tại.")
    except Exception as e:
        print(f"Lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()