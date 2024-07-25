import uuid
import io

def uploadImageToS3(s3_client,image_content: bytes,region):
    # 고유 식별 이름 생성
    unique_file_name = str(uuid.uuid4())
    file_location = f"taleimage/{unique_file_name}"

    # s3에 이미지 업로드
    s3_client.upload_fileobj(io.BytesIO(image_content), "iluvbook-bucket", file_location,ExtraArgs={
                'ContentType': "image/jpeg"
            })

    # file URL 정의
    file_url = f"https://iluvbook-bucket.s3.{region}.amazonaws.com/{file_location}"

    return file_url