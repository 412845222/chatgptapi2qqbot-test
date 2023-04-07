import nonebot
from nonebot.adapters.console import Adapter as ConsoleAdapter  # 避免重复命名


# 初始化 NoneBot
nonebot.init()


# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(ConsoleAdapter)


# 在这里加载插件
nonebot.load_builtin_plugins("echo")  # 内置插件
nonebot.load_from_toml("pyproject.toml")
# nonebot.load_plugin("thirdparty_plugin")  # 第三方插件
# nonebot.load_plugins("awesome_bot/plugins")  # 本地插件


if __name__ == "__main__":
    nonebot.run()