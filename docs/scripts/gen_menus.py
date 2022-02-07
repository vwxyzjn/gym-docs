__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

import sys
import os
sys.path.append("..")
menu = ["API", "Vector API", "Spaces", 
"environments", 
"Environment Creation", "Third Party Environments",
"Wrappers"]

env_type_images = {
    "Atari": "space_invaders",
    "Mujoco": "ant"
}

ret = "#AUTOGENERATED: EDIT gen_menus in _scripts\n"
for item in menu:
    if item != "environments":
        link = item.replace(" ", "_").lower()
        file = open(f"../pages/{link}/index.md", "r")
        text = file.read()
        splits = text.split("##")
        headers = []
        for chunk in splits:
            header = chunk.split("\n")[0].strip()
            # only ## headers
            if header[0] == "#":
                continue
            headers.append(header)
        
        headers = headers[1:]

        ret+= f"- title: {item}\n"
        link = item.replace(" ", "_").lower()
        ret+= f"  path: /{link}\n"
        if len(headers) > 0:
            ret+= "  sublinks: \n"
            for header in headers:
                ret+= f"    - title: \"{header}\"\n"
                link = header.replace(" ", "-").replace(".", "").replace("&", "").lower()
                ret+= f"      path: \"#{link}\"\n"

        ret+= "\n"
    # find environments :)
    else:
        ret+= "- title: Environments\n"
        ret+= "  path: /environments\n"
        ret+= "  sublinks:\n"
        
        dir = "../pages/environments"
        for filename in os.listdir(dir):
            f = os.path.join(dir, filename)
            # check if sub directory
            if os.path.isdir(f):
                env_type = os.path.basename(f)
                env_type_path = f"/{env_type}"
                if env_type == "box2d":
                    env_type_title = "Box2D"
                else:
                    env_type_title = env_type.replace("_", " ").title()
                ret+= f"   - title: \"{env_type_title}\"\n"
                ret+= f"     path: \"{env_type_path}\"\n"
                if env_type_title in env_type_images:
                    gif =  os.path.join(f, "videos", env_type_images[env_type_title] + ".gif").replace("pages/", "")
                else:
                    gif = os.path.join(f, "videos", os.listdir(os.path.join(f, "videos"))[0]).replace("pages/", "")
                
                ret+= f"     image: {gif}\n"
                ret+= f"     subsublinks: \n"
                envs_added = 0
                # go through environments
                listdir = [m for m in os.listdir(f) if m[-3:] == ".md" and m != "index.md"]
                for env_path in listdir:
                    if envs_added == 5:
                        env_path = ""
                        env_title = f"<strong>And {len(listdir)-5} more...</strong>"
                    else:
                        env_path = env_path[:-3]
                        env_title = env_path.replace("_", " ").title()
                        env_path = "/" + env_path
                    ret+= f"     - title: \"{env_title}\"\n"
                    ret+= f"       path: \"{env_path}\"\n"
                    if envs_added == 5:
                        break
                    envs_added+= 1

ret+= "#AUTOGENERATION ENDED"

print(ret)