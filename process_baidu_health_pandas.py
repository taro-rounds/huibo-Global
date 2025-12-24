import pandas as pd
import os

# 定义文件路径
file_path = "/Users/wangyucheng02/Documents/我的开放项目/IronMan/百度大健康广告.csv"

# 检查文件是否存在
if not os.path.exists(file_path):
    print(f"文件不存在: {file_path}")
    exit()

print("--- 开始读取文件 ---\n")

# 使用pandas读取文件
# 尝试不同的引擎和格式
print("尝试读取文件...")

# 首先尝试作为Excel文件读取
try:
    df = pd.read_excel(file_path, engine='openpyxl')
    print("✓ 成功以Excel格式读取文件")
except Exception as e:
    print(f"✗ 无法以Excel格式读取: {e}")
    # 尝试作为CSV文件读取
    try:
        df = pd.read_csv(file_path)
        print("✓ 成功以CSV格式读取文件")
    except Exception as e:
        print(f"✗ 无法以CSV格式读取: {e}")
        exit()

print(f"\n--- 文件读取成功 ---")
print(f"数据形状: {df.shape[0]} 行, {df.shape[1]} 列")
print(f"\n数据列名:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col}")

print(f"\n--- 数据预览 ---")
# 显示前5行数据
print("\n前5行数据:")
print(df.head())

print(f"\n--- 数据类型 ---")
print(df.dtypes)

# 处理前200条数据
print(f"\n--- 处理前200条数据 ---")

# 获取前200条数据
df_200 = df.head(200)
print(f"处理数据量: {len(df_200)} 条")

# 保存前200条数据到CSV文件
output_file = "/Users/wangyucheng02/Documents/我的开放项目/IronMan/百度大健康广告_前200条.csv"
df_200.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"\n--- 处理完成 ---")
print(f"前200条数据已保存到: {output_file}")
print(f"\n保存的数据包含以下列:")
for col in df_200.columns:
    print(f"  - {col}")

print(f"\n数据统计信息:")
print(df_200.describe())
