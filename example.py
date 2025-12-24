import json
import csv
import os

# 模拟批量数据（这里放入了你的原始数据，并模拟了第二条数据）
raw_data_list = [
    # 第一条数据 (你的原始数据)
    {
        "business_code":"TianShuAds_AI_tool",
        "callback":{"address":"http://api.baidu-int.com","path":"/json/sms/service/VideoShoppingAigcService/receiveHbxFrontVideo"},
        "goods_info":{"product_name":"【熊宝堂熊胆粉】口苦口干 失眠多梦 熬夜喝酒应酬伤肝 专业调理肝损伤脂肪肝酒精肝排肝毒"},
        "video_info":{"video_url":"http://example.com/video1.mp4"}
    },
    # 模拟第二条数据
    {
        "business_code":"TianShuAds_AI_tool",
        "callback":{"address":"http://api.test-server.com","path":"/test/path"},
        "goods_info":{"product_name":"【测试商品】自动生成视频测试"},
        "video_info":{"video_url":"http://example.com/video2.mp4"}
    }
]

print("--- 开始批量提取 ---")

# 循环提取
results = []
for index, item in enumerate(raw_data_list, 1):
    try:
        # 1. 提取 video_url (位于 video_info 下)
        # 使用 .get() 方法防止字段不存在时报错，默认返回 "未知视频地址"
        video_url = item.get('video_info', {}).get('video_url', '未知视频地址')
        
        # 2. 提取 product_name (位于 goods_info 下)
        product_name = item.get('goods_info', {}).get('product_name', '未知商品名')
        
        # 打印当前提取结果
        print(f"第 {index} 条数据:")
        print(f"  视频地址: {video_url}")
        print(f"  商品名: {product_name}\n")
        
        # 存入结果列表，方便后续导出
        results.append({"video_url": video_url, "product_name": product_name})
        
    except Exception as e:
        print(f"第 {index} 条数据解析出错: {e}")

print(f"--- 提取完成，共获取 {len(results)} 条结果 ---")

# 写入CSV文件
csv_filename = "extracted_data.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    # 定义CSV字段名
    fieldnames = ['video_url', 'product_name']
    # 创建CSV写入器
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # 写入表头
    writer.writeheader()
    # 写入数据行
    writer.writerows(results)

print(f"--- 数据已保存到CSV文件: {os.path.abspath(csv_filename)} ---")