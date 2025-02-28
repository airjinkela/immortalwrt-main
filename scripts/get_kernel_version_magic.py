import json
import argparse

file_path = ""
file_sava_path = ""
target = ""
sub_target = ""
kernel_version = ""

default_fail_magic_number = "12345678123456781234567812345678"

def load_json_from_file(json_file_path:str):
    try:
        with open(json_file_path, 'r') as f:
            return json.loads(f.read())
    except Exception as e:
        return False

def get_kernel_versions(in_json:list, s_target:str, s_sub_target:str):
    for target_fu in in_json:
        if target_fu["name"] == s_target:
            for sub_target_fu in target_fu["sub_targets"]:
                if sub_target_fu["name"] == s_sub_target:
                    return sub_target_fu["kernel_versions"]
    return False
    
def get_fit_kernel_magic(in_json:list, s_kernel_version:str):
    if(len(in_json)==1):
        return in_json[0]["kernel_magic"]
    for kernel_version_fn in in_json:
        if(kernel_version_fn["kernel_version"] == s_kernel_version):
            return kernel_version_fn["kernel_magic"]
    return False

def get_kernel_magic_from_file(s_file_path, s_target:str, s_sub_target:str, s_kernel_version:str):
    json_load = load_json_from_file(s_file_path)
    if json_load == False:
        return default_fail_magic_number
    
    kernel_versions = get_kernel_versions(json_load, s_target, s_sub_target)
    if kernel_version == False:
        return default_fail_magic_number
    
    kernel_magic = get_fit_kernel_magic(kernel_versions, s_kernel_version)
    if kernel_magic == False:
        return default_fail_magic_number
    
    return kernel_magic
import os

def silent_file_write_with_dir(fp: str, content: str) -> bool:
    try:
        # 自动创建父目录
        # os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(e)
        return False

def main():
    kernel_magic = get_kernel_magic_from_file(file_path, target, sub_target, kernel_version)
    # print(kernel_magic)
    silent_file_write_with_dir(file_sava_path, kernel_magic)

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='file_path')
    parser.add_argument('file_sava_path', type=str, help='file_save_path')
    parser.add_argument('target', type=str, help='targrt')
    parser.add_argument('sub_target', type=str, help='sub target')
    parser.add_argument('kernel_version', type=str, help='kernel version')
    args = parser.parse_args()

    file_path = args.file_path
    file_sava_path = args.file_sava_path
    target = args.target
    sub_target = args.sub_target
    kernel_version = args.kernel_version
    # print("aaaaaaaaaa",file_path,file_sava_path,target,sub_target,kernel_version)
    main()