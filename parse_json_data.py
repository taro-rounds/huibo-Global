import json
import pandas as pd
import csv
import os

# 定义文件路径
input_file = "/Users/wangyucheng02/Documents/我的开放项目/IronMan/百度大健康广告.csv"
output_file = "/Users/wangyucheng02/Documents/我的开放项目/IronMan/百度大健康广告_提取结果.csv"

print("--- 开始批量提取 Video URL 和 Product Name ---")

# 检查文件是否存在
if not os.path.exists(input_file):
    print(f"文件不存在: {input_file}")
    exit()

# 使用pandas读取文件（处理Excel格式的CSV文件）
try:
    # 尝试作为Excel文件读取
    df = pd.read_excel(input_file, engine='openpyxl')
    print(f"✓ 成功读取文件，共 {len(df)} 条数据")
except Exception as e:
    print(f"✗ 无法读取文件: {e}")
    exit()

results = []

# 处理前200条数据
total_rows = min(200, len(df))

for index in range(total_rows):
    try:
        # 获取当前行数据
        row = df.iloc[index]
        
        # 提取input_params列的JSON字符串
        input_params = row.get('input_params', '')
        
        if not input_params:
            print(f"[{index+1}] 无JSON数据")
            continue
        
        # 解析JSON
        data = json.loads(input_params)
        
        # 1. 提取 video_url
        # 检查video_url是否在最外层
        if 'video_url' in data:
            video_url = data.get('video_url', '无视频链接')
        # 否则检查是否在video_info中
        else:
            video_url = data.get('video_info', {}).get('video_url', '无视频链接')
        
        # 2. 提取 product_name
        product_name = data.get('goods_info', {}).get('product_name', '无商品名')
        
        # 打印提取结果
        print(f"[{index+1}] 视频链接: {video_url}")
        print(f"    商品名称: {product_name}")
        print("-" * 50)
        
        results.append([video_url, product_name])
        
    except json.JSONDecodeError as e:
        print(f"[{index+1}] JSON解析错误: {e}")
    except Exception as e:
        print(f"[{index+1}] 数据解析出错: {e}")

# 保存到CSV文件
with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['Video URL', 'Product Name'])
    writer.writerows(results)

print(f"--- 提取完成，共处理 {total_rows} 条数据，成功提取 {len(results)} 条结果 ---")
print(f"结果已保存到: {output_file}")