"""
内置站点资料结构化摘要生成工具
读取内置站点配置并输出结构化摘要，包括关键词、URL、标签和简短说明。
"""

import json
from typing import List, Dict, Optional

# 内置站点资料配置
SITE_DATA = [
    {
        "name": "乐鱼体育",
        "url": "https://officialindex-leyu.com.cn",
        "keywords": ["乐鱼体育", "体育平台", "赛事直播"],
        "tags": ["体育", "在线直播", "竞技"],
        "description": "乐鱼体育是专业的体育赛事平台，提供实时比分与高清直播服务。"
    },
    {
        "name": "资讯聚合站",
        "url": "https://news.aggregator.example.com",
        "keywords": ["新闻", "资讯", "聚合", "每日更新"],
        "tags": ["新闻", "聚合", "信息流"],
        "description": "全领域新闻资讯聚合平台，覆盖科技、娱乐、体育等多类内容。"
    }
]


class SiteSummary:
    """站点摘要数据类"""

    def __init__(self, name: str, url: str, keywords: List[str], tags: List[str], description: str):
        self.name = name
        self.url = url
        self.keywords = keywords
        self.tags = tags
        self.description = description

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "url": self.url,
            "keywords": self.keywords,
            "tags": self.tags,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "SiteSummary":
        return cls(
            name=data["name"],
            url=data["url"],
            keywords=data.get("keywords", []),
            tags=data.get("tags", []),
            description=data.get("description", "")
        )

    def format_summary(self) -> str:
        """生成格式化的摘要文本"""
        keyword_str = ", ".join(self.keywords)
        tag_str = ", ".join(self.tags)
        lines = [
            f"站点名称: {self.name}",
            f"URL: {self.url}",
            f"关键词: {keyword_str}",
            f"标签: {tag_str}",
            f"简介: {self.description}",
            "-" * 40
        ]
        return "\n".join(lines)


def load_site_data(data_list: Optional[List[Dict]] = None) -> List[SiteSummary]:
    """从内置数据或传入列表加载站点摘要对象列表"""
    source = data_list if data_list is not None else SITE_DATA
    return [SiteSummary.from_dict(item) for item in source]


def generate_structured_summaries(sites: List[SiteSummary]) -> List[Dict]:
    """生成结构化摘要列表（字典格式）"""
    return [site.to_dict() for site in sites]


def generate_text_summaries(sites: List[SiteSummary]) -> str:
    """生成可读的文本摘要"""
    parts = [site.format_summary() for site in sites]
    return "\n".join(parts)


def export_to_json(sites: List[SiteSummary], indent: int = 2) -> str:
    """将站点摘要导出为JSON字符串"""
    dict_list = generate_structured_summaries(sites)
    return json.dumps(dict_list, ensure_ascii=False, indent=indent)


def main():
    """主函数：读取内置站点资料并输出结构化摘要"""
    print("=== 内置站点资料结构化摘要 ===")
    print()

    # 读取内置站点数据
    site_objects = load_site_data()

    # 输出文本摘要
    print("[文本摘要]")
    print(generate_text_summaries(site_objects))

    # 输出结构化JSON摘要
    print("[JSON摘要]")
    json_output = export_to_json(site_objects)
    print(json_output)

    # 演示：额外传入自定义站点
    custom_data = [
        {
            "name": "示例站点",
            "url": "https://example.com",
            "keywords": ["示例", "测试"],
            "tags": ["demo", "test"],
            "description": "这是一个示例站点，用于演示扩展能力。"
        }
    ]
    custom_sites = load_site_data(custom_data)
    print("[自定义站点摘要]")
    print(generate_text_summaries(custom_sites))


if __name__ == "__main__":
    main()