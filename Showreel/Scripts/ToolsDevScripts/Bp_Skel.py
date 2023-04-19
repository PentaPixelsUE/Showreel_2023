import unreal

def check_files():
    reg = unreal.AssetRegistryHelpers.get_asset_registry()
    eal = unreal.EditorAssetLibrary()
    dir_path = '/Game/ToolsDev/SkeletalMeshes/'
    skelmeshes = []

    if eal.does_directory_exist(dir_path):
        assets = reg.get_assets_by_path(dir_path, recursive=False)
        for asset in assets:
            full_name=asset.get_full_name()
            path = full_name.split(' ')[-1]
            skelmesh = unreal.load_asset(path)

            if isinstance(skelmesh, unreal.SkeletalMesh):
                skelmeshes.append(skelmesh)
        return skelmeshes
    else:
        print("Directory does not exist.")
        return []

check_files()

