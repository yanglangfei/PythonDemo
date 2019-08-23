from faker import Faker
from faker.providers import internet

##  https://faker.readthedocs.io/en/master/locales/zh_CN.html
## https://faker.readthedocs.io/en/master/communityproviders.html
# https://faker.readthedocs.io/

faker = Faker('zh_CN')
# 安装  Provider
faker.add_provider(internet)
print(faker.ipv4_private())
# 生成随机姓名
print(faker.name())
# 生成女性名称
print(faker.name_female())
# 生成男性名称
print(faker.name_male())
# 生成随机地址
print(faker.address())
# 生成随机颜色名称
print(faker.color_name())
# 生成随机公司名称
print(faker.company())
# 生成随机信用卡信息
print(faker.credit_card_full(card_type=None))
# 生成随机时间
print(faker.date(pattern="%Y-%m-%d", end_datetime=None))
# 生成随机文件信息
print(faker.file_path(depth=1, category=None, extension=None))
# 生成随机经纬度位置信息
print(faker.local_latlng(country_code="CN", coords_only=False))
# 生成随机邮箱
print(faker.ascii_company_email())
print(faker.ascii_email())
print(faker.ascii_free_email())
# 生成随机IP
print(faker.ipv4_private(network=False, address_class=None))
print(faker.ipv4_public(network=False, address_class=None))
# 生成随机URL
print(faker.uri())
print(faker.url(schemes=None))
# 生成随机用户名
print(faker.user_name())
# 生成随机工作
print(faker.job())
# 生成随机文本
print(faker.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None))
print(faker.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))
print(faker.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None))
print(faker.words(nb=3, ext_word_list=None, unique=False))
# 随机密码
print(faker.md5(raw_output=False))
print(faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
print(faker.sha256(raw_output=False))
faker.uuid4(cast_to=str)
# 生成随机 User-Agent
print(faker.chrome(version_from=13, version_to=63, build_from=800, build_to=899))
print(faker.firefox())
print(faker.internet_explorer())
print(faker.user_agent())
print(faker.linux_platform_token())
print(faker.mac_platform_token())
print(faker.opera())
print(faker.safari())
print(faker.windows_platform_token())
