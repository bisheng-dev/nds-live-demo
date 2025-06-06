import boto3
from generated.nds_live_tile.tile import Tile  # 替换为你的实际生成路径

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # 下载文件
    obj = s3.get_object(Bucket=bucket, Key=key)
    data = obj['Body'].read()
    
    # 处理数据（示例：打印文件大小）
    print(f"Processed {key}, size: {len(data)} bytes")
    
    return {'statusCode': 200}
