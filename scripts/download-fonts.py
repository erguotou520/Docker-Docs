import os
import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import unquote

def download_font(url):
    # 从URL中提取文件名
    filename = unquote(url.split('/')[-1])
    
    try:
        # 发送GET请求下载字体文件
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # 确保下载目录存在
        os.makedirs('fonts', exist_ok=True)
        
        # 保存文件
        file_path = os.path.join('fonts', filename)
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f'成功下载: {filename}')
        
    except Exception as e:
        print(f'下载 {filename} 时出错: {str(e)}')

def main():
    # 字体文件URL列表
    font_urls = [
        # 思源宋体
        "https://raw.githubusercontent.com/wordshub/free-font/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E5%AE%8B%E4%BD%93/SourceHanSerifCN-Bold.ttf",
        "https://raw.githubusercontent.com/wordshub/free-font/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E5%AE%8B%E4%BD%93/SourceHanSerifCN-ExtraLight.ttf",
        "https://raw.githubusercontent.com/wordshub/free-font/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E5%AE%8B%E4%BD%93/SourceHanSerifCN-Heavy.ttf",
        "https://raw.githubusercontent.com/wordshub/free-font/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E5%AE%8B%E4%BD%93/SourceHanSerifCN-Light.ttf",
        "https://raw.githubusercontent.com/wordshub/free-font/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E5%AE%8B%E4%BD%93/SourceHanSerifCN-Medium.ttf",
        "https://raw.githubusercontent.com/wordshub/free-font/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E5%AE%8B%E4%BD%93/SourceHanSerifCN-Regular.ttf",
        "https://raw.githubusercontent.com/wordshub/free-font/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E5%AE%8B%E4%BD%93/SourceHanSerifCN-SemiBold.ttf",
        
        # 思源黑体
        "https://github.com/wordshub/free-font/raw/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E9%BB%91%E4%BD%93/SourceHanSansCN-Bold.otf",
        "https://github.com/wordshub/free-font/raw/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E9%BB%91%E4%BD%93/SourceHanSansCN-ExtraLight.otf",
        "https://github.com/wordshub/free-font/raw/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E9%BB%91%E4%BD%93/SourceHanSansCN-Heavy.otf",
        "https://github.com/wordshub/free-font/raw/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E9%BB%91%E4%BD%93/SourceHanSansCN-Light.otf",
        "https://github.com/wordshub/free-font/raw/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E9%BB%91%E4%BD%93/SourceHanSansCN-Medium.otf",
        "https://github.com/wordshub/free-font/raw/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E9%BB%91%E4%BD%93/SourceHanSansCN-Normal.otf",
        "https://github.com/wordshub/free-font/raw/refs/heads/master/assets/font/%E4%B8%AD%E6%96%87/%E6%80%9D%E6%BA%90%E5%AD%97%E4%BD%93%E7%B3%BB%E5%88%97/%E6%80%9D%E6%BA%90%E9%BB%91%E4%BD%93/SourceHanSansCN-Regular.otf",
    ]
    
    # 使用线程池进行并发下载
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download_font, font_urls)

if __name__ == '__main__':
    main()
