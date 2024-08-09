import platform


def get_sys_info():
    """
    获取操作系统信息，如果是 Windows，内核为空
    @return: (操作系统, 位数, 内核)
    """
    # 操作系统
    _ = platform.system()
    sys_name = "MacOS" if _ == "Darwin" else _
    # 不是 MacOS 或者 Windows
    if sys_name not in ["MacOS", "Windows"]:
        print("{:*^80}".format("暂不支持你的电脑型号，请联系相关老师解决！"))
        return

    # 系统位数
    sys_bit = platform.architecture()
    # 系统版本
    sys_version = ""
    # MacOS
    if sys_name == "MacOS":
        _ = platform.version()
        if "X86_64" in _:
            sys_version = "Intel"
        elif "ARM" in _:
            sys_version = "M1/M2"
    elif sys_name == "Windows":
        pass

    sys_info = sys_name, sys_bit[0], sys_version
    print(f"{'*' * 80}")
    print(f"电脑的操作系统是：{sys_info}")

    return sys_info


if __name__ == '__main__':
    res = get_sys_info()
