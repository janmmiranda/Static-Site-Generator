import os, shutil

def copy_dir(dir_path_source, dir_path_target):
    src_path_exists = os.path.exists(dir_path_source)
    target_path_exists = os.path.exists(dir_path_target)
    print(f"source dir: {dir_path_source} exists: {src_path_exists}")
    print(f"target dir: {dir_path_target} exists: {target_path_exists}")

    if not src_path_exists:
        print(f"Exiting as source dir {dir_path_source}, does not exists")
        return
    else:
        # check if target exists, if so delete it
        if target_path_exists:
            target_contents_old = os.listdir(dir_path_target)
            print(f"deleting content: {target_contents_old} of {dir_path_target}")
            shutil.rmtree(dir_path_target)

        # create new target dir
        print(f"creating new dir {dir_path_target}")
        os.mkdir(dir_path_target)

        source_content = os.listdir(dir_path_source)
        print(f"attempting to copy: {source_content}")

        for item in source_content:
            old_path = dir_path_source
            new_path = dir_path_target
            if not old_path.endswith("/"):
                old_path += "/"
            old_path += item
            if not new_path.endswith("/"):
                new_path += "/"
            new_path += item
            is_file = os.path.isfile(old_path)
            print(f"{old_path} is a file: {is_file}")
            if is_file:
                print(f"attempting to copy {old_path} to {new_path}")
                shutil.copy(old_path, new_path)
                print(f"target contents: {os.listdir(dir_path_target)}")
            else:
                print(f"{old_path} is a directory, creating {new_path} in target")
                os.mkdir(new_path)
                print(f"current target contents: {os.listdir(dir_path_target)}")
                print(f"copying contents of {old_path} into {new_path}")
                copy_dir(old_path, new_path)


            
    
