# https://docs.langflow.org/contributing/how-contribute
Docker
Đoạn mã sau sẽ chạy phần phụ trợ và giao diện người dùng trong các vùng chứa riêng biệt. Giao diện người dùng sẽ có sẵn tại localhost:3000và phần phụ trợ tại localhost:7860.

docker compose up --build
# or
make dev build=1

Tài liệu được xây dựng bằng Docusaurus . Để chạy tài liệu cục bộ, hãy chạy các lệnh sau:

cd docs
npm install
npm run start

Tài liệu sẽ có sẵn tại localhost:3000và tất cả các tệp đều nằm trong docs/docsthư mục. Khi bạn đã thực hiện xong các thay đổi của mình, bạn có thể tạo Yêu cầu kéo tới mainnhánh.