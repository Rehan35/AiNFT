import openai
import requests
import time
import numpy as np

openai.api_key = "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"

midjounrey_api_key = "628d9c17-1c06-4df5-9fdb-084495b263df"

themes = ["Pixelated", "Cyber", "Glitch", "Neon", "Abstract", "Surreal", "Holographic", "Virtual", "Interstellar", "Synthwave", "Transcendent", "Interactive"]
ideas = ["NBA", "Cars", "Sports", "Entertainment", "Netflix", "Towers"]

midjourney_image_url = "https://api.midjourneyapi.io/v2/imagine"
midjourney_result_url = "https://api.midjourneyapi.io/v2/result"
midjourney_upscale_url = "https://api.midjourneyapi.io/v2/upscale"

prompt = "Design an NBA championship ring from the 1990s, incorporating distinct elements from a winning team."

headers = {"content-type": "application/json; charset=UTF-8",'Authorization':'{}'.format(midjounrey_api_key)}

for i in range(1) :
    theme = np.random.choice(themes, size=1, replace=True)
    idea = np.random.choice(ideas, size=1, replace=True)
    prompt = "Generate 1 image generation prompt about {} {}".format(theme[0], idea[0])
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": prompt}
        ]
    )
    image_prompts = response["choices"][0]["message"]["content"].splitlines()
    for prompt in image_prompts :
        index = prompt.find(" ")
        print("Prompt: {}".format(prompt[index+1:len(prompt) - 1]))
        # image = openai.Image.create(prompt=prompt[index+1:len(prompt) - 1], n = 1, size= "512x512")
        # print(image)
        r = requests.post(midjourney_image_url, json={
        "prompt": prompt
        }, headers=headers)

        print(r.content)


# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages = [
#         {"role": "user", "content": "Generate 10 image generation prompts about vintage NBA"}
#     ]
# )

# print(response["choices"][0]["message"]["content"].splitlines())

image_prompts = ['1. Design a retro-inspired NBA poster featuring iconic players from the 1980s.', 
                 '2. Create a vintage-style trading card of a legendary NBA team from the 1960s.', 
                 '3. Illustrate a classic NBA arena from the 1970s, highlighting its unique architecture and atmosphere.', 
                 "4. Design a throwback NBA jersey for a current player, paying homage to a team's historical design.", 
                 '5. Create a psychedelic artwork capturing the energy and spirit of the ABA (American Basketball Association) era.', 
                 '6. Illustrate a vintage-inspired NBA basketball shoe, blending old-school aesthetics with modern technology.', 
                 '7. Design an NBA championship ring from the 1990s, incorporating distinct elements from a winning team.', 
                 '8. Create a vintage-style comic book cover featuring an NBA player as a superhero with unique basketball-related powers.', 
                 '9. Illustrate an iconic NBA moment from the 1980s using a vintage-style pop art approach.', 
                 "10. Design a retro-inspired basketball court, featuring vibrant colors and patterns reminiscent of the NBA's early days."]
# for prompt in image_prompts :
#     index = prompt.find(" ")
#     print(prompt[index+1:])

metadata = {
    "name": "Futuristic Cityscape with Sleek Towers",
    "description": "A futuristic cityscape emerges, adorned with sleek towers that pierce the sky, symbolizing innovation and elegance. The architectural marvels captivate with their seamless blend of modernity and visionary design, creating a mesmerizing vista of tomorrow's urban landscape.",
    "image": "https://cdn.discordapp.com/attachments/1123751566474760262/1125643214053978162/yodan_Create_an_image_of_a_futuristic_cityscape_with_sleek_towe_8bd42941-92e4-4da9-a478-3af602c0a728.webp"
}

# r = requests.post(midjourney_image_url, json={
#   "prompt": prompt
# }, headers=headers)

# print(r.content)

# taskId = "{}".format(r.text[11:len(r.text)-2])

#https://cdn.discordapp.com/attachments/1123751566474760262/1125643214053978162/yodan_Create_an_image_of_a_futuristic_cityscape_with_sleek_towe_8bd42941-92e4-4da9-a478-3af602c0a728.webp
#https://cdn.midjourney.com/1c864c39-e4bc-4d8e-820c-d24e7de934c1/0_0.png
#https://cdn.discordapp.com/attachments/1123751566474760262/1125984953356791879/olivier_Illustrate_an_iconic_NBA_moment_from_the_1980s_using_a__0af107f8-7cad-4491-94e3-61480bf95853.webp
#https://cdn.discordapp.com/attachments/1123751566474760262/1125993318204055644/njho_Design_a_throwback_NBA_jersey_for_a_current_player_paying__5e43b0c2-febc-496b-9bfd-81b2db766520.png
#https://cdn.discordapp.com/attachments/1123751566474760262/1125994656342233178/olivier_Illustrate_a_vintage-inspired_NBA_basketball_shoe_blend_dd65e3a1-36fa-496c-bb14-63d8d3124ea6.png
#https://cdn.discordapp.com/attachments/1123751566474760262/1125995586773069894/olivier_Design_an_NBA_championship_ring_from_the_1990s_incorpor_df638731-3376-4ef6-b3b1-883937919617.png
#https://cdn.discordapp.com/attachments/1123751566474760262/1127812733497249792/yodan_Design_a_retro-inspired_basketball_court_featuring_vibran_e1cc8e56-687c-43c9-9ff5-fcb34b769406.png
#https://cdn.discordapp.com/attachments/1123751566474760262/1127813796115791872/yodan_Create_a_vintage-style_trading_card_of_a_legendary_NBA_te_343c8f0c-aa02-4a2d-badb-4380361a6cc2.png
#https://cdn.discordapp.com/attachments/1123751566474760262/1127814908726227075/yodan_Create_a_cool_nike_jordan_1_shoe_design___406797405420098_a1e4d04b-1208-4a32-9345-90d2e34095ed.png
#https://cdn.discordapp.com/attachments/1123751566474760262/1127816822150926337/yodan_generate_an_image_about_michael_jordan_slamming_a_dunk____5c2dd01c-e69e-4280-9b94-c79c8ae67011.png
#https://cdn.discordapp.com/attachments/1123751566474760262/1127817454211575849/yodan_generate_cool_images_of_Stephen_Curry_hitting_crazy_three_4799e0fc-4ddb-46a9-b2c9-afda4bda8c7d.png
#https://cdn.discordapp.com/attachments/1123751566474760262/1127818058417836173/yodan_Generate_an_image_about_the_show_suits___8683201906282982_8a033aaa-7596-4a98-be7e-14eb7474d123.png 

# time.sleep(60)

# r = requests.post(midjourney_result_url, json={
#   "taskId": taskId
# }, headers=headers)

# print(r["imageURL"])

# print(r.content)

# print(r.text[13:len(r.text) - 2])
# print(r["taskId"])

# u = requests.post(midjourney_upscale_url, json={
#   "position": 1,
#   "taskId": taskId
# }, headers=headers)

# print(u.content)

# image_resp = openai.Image.create(prompt=" Create an image of a futuristic cityscape with sleek, towering skyscrapers and advanced transport systems.",
#                                   n=1, size="512x512")

# print(image_resp)


