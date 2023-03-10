import os

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files='config.json',
    environments=True
)

# 设置环境变量的方法#######################################################################################################

# # 方法a: 在代码中直接设置
# os.environ['ENV_FOR_DYNACONF'] = 'local'
# os.environ['ENV_FOR_DYNACONF'] = 'development'
# os.environ['ENV_FOR_DYNACONF'] = 'production'
# print('age值为:{}'.format(settings.age))

# 方法b: 在pycharm-->run-->配置-->环境变量  ENV_FOR_DYNACONF='local' 可不加引号 如果前边有变量 需要在前一个变量后边增加一个;
# 例如PYTHONUNBUFFERED=1;ENV_FOR_DYNACONF='local'
print('age值为:{}'.format(settings.age))

# 方法c: 命令行执行 python get_config.py ENV_FOR_DYNACONF='local'

# 方法d: Dockerfile设置 ENV ENV_FOR_DYNACONF local
