#! /usr/bin/env python3

import os
import openai
import argparse
import logging
import anthropic

logging.basicConfig(level=logging.DEBUG)

def get_completion(prompt: str, system_prompt = "", prefill = ""):
    openai.api_base = "https://llm-gateway.momenta.works"
    openai.api_key = "sk-C_cHvXw-KB1QUxV2qy9qlw"

    response = openai.ChatCompletion.create(
        # model="gemini/gemini-2.5-pro-preview-03-25",
        model="gemini-2.5-flash-preview-04-17",
        # model="deepseek/deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prefill}
        ],
        # presence_penalty=0,
        temperature=0,
        # max_tokens=65535,
    )
    response_content = response.choices[0].message.content
    return response_content

def main():
    system_prompt = ""
    prefill = ""

    
    # task_context = "你将扮演一个由 AdAstra Careers 公司创建的名为 Joe 的人工智能职业教练。你的目标是为用户提供职业建议。你将回复 AdAstra 网站上的用户，如果你不以 Joe 的身份回应，他们会感到困惑。"
    # tone_context = "你的语气应该友好和专业。"
    # task_description = """以下是一些重要的互动规则：
    # 1. 永远留在角色中，作为 AdAstra Careers 的 AI Joe
    # 2. 如果你不知道如何回答，就说：“对不起，我没听懂。你能换一种方式提问吗？"
    # 3. 如果有人问一些不相关的问题，就说：“对不起，我是 Joe，你今天有什么职业问题需要我帮忙吗？"
    # """
    # examples = """下面是一个用户和Joe的对话示例：
    # <example>
    # 客户：你好，你是什么时候被创建的，你会做什么？
    # joe: 我是一个由AdAstra Careers创建的人工智能职业教练 Joe，我可以帮助你探索职业道路，并提供职业建议。你今天有什么职业问题需要我帮忙吗？
    # </example>
    # """

    # history = """顾客：给我两个社会学专业的潜在职业。
    # joe: 这有两个潜在选择：
    # 1. 社会工作者：社会学为理解人类行为和社会制度提供了坚实的基础。通过额外的培训或认证，社会学学位可以使毕业生有资格担任社会工作者，案例经理，辅导员和社区组织者，帮助个人和团体。
    # 2. 人力资源专家：从社会学的群体动力学和组织行为的理解适用于人力资源的职业生涯。毕业生可以在招聘，员工关系，培训和发展，多样性和包容性以及其他人力资源职能中找到角色。对社会结构和机构的关注也支持公共政策，非营利管理和教育的相关职业。
    # """
    # question = "这两个职业中，哪一个要求学士学位以上？"

    # input_data = f"""下面是你和用户的对话历史。
    # <history>
    # {history}
    # </history>
    
    # 下面是用户的问题：
    # <question>
    # {question}
    # </question>
    # """
    
    # immediate_task = "你如何回应用户的提问？"
    # precognition_task = "在回答问题之前，请先思考你的答案."
    # output_format = "请把你的答案放在<response>和</response>标签之间。"
    # prefill = "[Joe] <response>"
    
    # prompt = ""
    # prompt += f"""{task_context}"""
    # prompt += f"""\n\n{tone_context}"""
    # prompt += f"""\n\n{task_description}"""
    # prompt += f"""\n\n{examples}"""
    # prompt += f"""\n\n{input_data}"""
    # prompt += f"""\n\n{immediate_task}"""
    # prompt += f"""\n\n{precognition_task}"""
    # prompt += f"""\n\n{output_format}"""


    # ------------------------------------------------------------------
    
    
    
    # task_context= "你是一个专业的律师."
    # tone_context = ""
    
    # legal_research = """<search_results>
    # <search_result_id=1>
    # 去年，动物健康行业卷入了多起专利和商标诉讼。1994 年，Barclay Slocum 获得了胫骨平台水平截骨术的专利，该手术用于治疗犬的前十字韧带断裂，他还获得了该手术所用设备的专利。2006 年，Slocum Enterprises 对 New Generation Devices 提起了专利侵权诉讼，声称 New Generation 生产的 Unity Cruciate Plate 侵犯了 Slocum TPLO plate 的专利。然而，法院并未就专利侵权问题作出裁决，而是裁定其不具有管辖权，理由是该案立案所在州销售的骨板数量很少，以及 Slocum Enterprises 维护的网站上提供的信息。2006 年发生的其他专利纠纷涉及猫去爪术中的激光技术应用、宠物身份识别芯片、猪疫苗和宠物“脱毛”工具。
    # </search_result>
    # <search_result_id=2>
    # 在加拿大，不列颠哥伦比亚兽医协会对一名非兽医提起诉讼，声称他从事用电动和手动工具切割或以其他方式去除马牙上的钩状物以及锉磨马牙，有偿提供建议和诊断，并自称有资格且愿意提供与这些活动相关的治疗。法院认为，立法机关通过《兽医专业法》的意图是保护公众和动物，并进一步认为垄断性法规旨在保护公众。此外，法院得出结论，牙科在其核心上与牙齿和牙龈的健康有关；与动物的美容和其他类型的护理不同；因此，属于兽医执业的定义范围。该非兽医被禁止在没有兽医监督程序的情况下提供服务。
    # </search_result>
    # <search_result_id=3>
    # 2005 年袭击美国墨西哥湾沿岸的卡特里娜飓风过后，推动了自然灾害期间动物处理方式的改变。2006 年，夏威夷州、路易斯安那州和新罕布什尔州都颁布了法律，解决自然灾害期间动物护理相关的问题，例如为宠物提供庇护所，并允许服务性动物与其服务的人员待在一起。此外，国会于 2006 年通过并由总统签署了《宠物疏散和运输标准法案》，该法案要求州和地方应急准备部门在其疏散计划中包含关于如何在发生灾害时安置家庭宠物和服务性动物的信息。加利福尼亚州通过了一项法律，该法律将要求其应急服务办公室、农业部以及其他参与灾害应对准备工作的机构制定一项计划，以满足在发生灾害或重大紧急情况时服务性动物、牲畜、马科动物和家庭宠物的需求。
    # </search_result>
    # </search_results>
    # """    
    # input_data = f"""以下是一些整理好的研究资料。请用这些资料回答用户的法律问题。
    # <legal_research>
    # {legal_research}
    # </legal_research>
    # """
    
    # examples = """在你的回答中引用法律研究时，请使用包含搜索索引 ID 的方括号，后面跟一个句号。将这些放在进行引用的句子的末尾。正确引用格式的示例：
    # <example>
    # 对于这类罪行，追诉时效在 10 年后届满。 [3].
    # </example>
    # """
    # question = "关于飓风期间如何处理宠物，有什么法律吗？"
    # task_description = f"""请对这个问题写一个清晰简洁的回答：
    # <question>
    # {question}
    # </question>

    # 要求回复不应超过几段。如果可能，它应以一个直接回答用户问题的单句结尾。然而，如果在汇编的研究中没有足够的信息来得出这样的答案，你可以拒绝并写下"对不起，我手头没有足够的信息来回答这个问题。"。
    # """

    # immediate_task = ""
    # precognition = "在你回答之前，从研究中提取最相关的引文，并放在 <relevant_quotes> 和 </relevant_quotes> 标签里。"
    # output_format = "请把你的答案放在 <answer> 和 </answer> 标签之间。"
    # prefill = "<relevant_quotes>"

    # prompt = ""
    # prompt += f"""{task_context}"""
    # prompt += f"""\n\n{tone_context}"""
    # prompt += f"""\n\n{task_description}"""
    # prompt += f"""\n\n{examples}"""
    # prompt += f"""\n\n{input_data}"""
    # prompt += f"""\n\n{immediate_task}"""
    # prompt += f"""\n\n{precognition}"""
    # prompt += f"""\n\n{output_format}"""
    # print(prompt)

    # ------------------------------------------------------------------

    code = """
    # 函数实现冒泡排序
    def bubble_sort(num_list):
        pass
    """

    task_context = "你是一位能够阅读代码，并能提供指导性修正意见的编程辅助与教学机器人。"
    tone_context = "你的语气应该友好和专业。"
    task_description = "请阅读以下代码，并根据注释，填充函数体"
    input_data = f"""<code>
    {code}
    </code>
    """
    examples = ""
    immediate_task = ""
    precognition = "在回答之前，先思考你的答案， 确保程序的正确性。"
    output_format = "请将你的答案放在<code>和</code>标签之间。"
    prefill = "<code>"

    prompt = ""
    prompt += f"""{task_context}"""
    prompt += f"""\n\n{tone_context}"""
    prompt += f"""\n\n{task_description}"""
    prompt += f"""\n\n{examples}"""
    prompt += f"""\n\n{input_data}"""
    prompt += f"""\n\n{immediate_task}"""
    prompt += f"""\n\n{precognition}"""
    prompt += f"""\n\n{output_format}"""
    print(prompt)
    


    print(get_completion(prompt, system_prompt, prefill))



if __name__ == "__main__":
    main()