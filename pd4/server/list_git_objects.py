import subprocess

def get_git_objects():
    try:
        # Получаем список всех объектов (коммитов, деревьев и blobs)
        result = subprocess.run(['git', 'rev-list', '--all'], 
                                capture_output=True, text=True, check=True)
        commits = result.stdout.splitlines()

        objects = {}
        for commit in commits:
            # Получаем содержимое коммита
            commit_info = subprocess.run(['git', 'cat-file', '-p', commit], 
                                          capture_output=True, text=True, check=True)
            objects[commit] = {'commit_info': commit_info.stdout, 'tree_info': {}}
            
            # Получаем дерево, связанное с коммитом
            tree_info = subprocess.run(['git', 'cat-file', '-p', commit + '^{tree}'], 
                                        capture_output=True, text=True, check=True)
            objects[commit]['tree_info'] = tree_info.stdout
            
            # Разделяем дерево на объекты
            tree_lines = tree_info.stdout.splitlines()
            file_objects = []
            for line in tree_lines:
                # Извлекаем тип и хеш объекта
                parts = line.split()
                if len(parts) >= 3:
                    object_type = parts[1]
                    object_hash = parts[2]
                    object_content = subprocess.run(['git', 'cat-file', '-p', object_hash], 
                                                     capture_output=True, text=True, check=True)
                    file_objects.append({'type': object_type, 'hash': object_hash, 'content': object_content.stdout, 'name': parts[3]})

            objects[commit]['files'] = file_objects

        return objects

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def print_objects(objects):
    if objects:
        for commit, data in objects.items():
            print(f"Commit: {commit}")
            print(data['commit_info'])
            print("Tree:")
            print(data['tree_info'])
            
            print("Files:")
            for file in data['files']:
                print(f"  Type: {file['type']}")
                print(f"  Hash: {file['hash']}")
                print(f"  Name: {file['name']}")
                print(f"  Content:\n{file['content']}")
                print("-" * 40)

            print("=" * 40)
            print('\n')  # Additional separator for better clarity

if __name__ == "__main__":
    git_objects = get_git_objects()
    print_objects(git_objects)
