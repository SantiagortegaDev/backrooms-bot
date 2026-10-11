import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import time
import asyncio

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot('b!', intents=intents)

class lobbycontainer(discord.ui.LayoutView):    
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="**Are you sure?**"),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="yes",
                    custom_id="button-start",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="yes",
                    custom_id="button-start2",
                ),
        ),
    )

class Level_1_n1(discord.ui.LayoutView):
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:30"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_1.png",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content="**Radio | Supervisor:** follow the line we marked on the floor to exit\n**Radio | John:**  we lost the team, i hope they arrive too"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Continue walking",
                    custom_id="button-continue-walking",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Say: \"how long until we leave?\"",
                    custom_id="button-how-long-until-we-leave",
                ),
        ),
    )

class Level_1_n2(discord.ui.LayoutView):
  def __init__(self, user):
    super().__init__()    
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:30"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_2.png",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content=f"**{user}:** how long until we leave?\n**John:** we're about to reach Sector 7 **\\*sigh*** it won't be long now."),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Continue walking",
                    custom_id="button-continue-walking",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Say: \"how long until we leave?\"",
                    disabled=True,
                    custom_id="button-how-long-until-we-leave",
                ),
        ),
    )
    self.add_item(container1)

class Level_1_n3(discord.ui.LayoutView):    
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:33"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_3.png",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    disabled=True,
                    custom_id="573ed2c54f374686c8beef2714381c8f",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    disabled=True,
                    custom_id="a901ab7a10dc4a9398df20b2a2fd562d",
                ),
        ),
    )

class Level_1_n4(discord.ui.LayoutView):    
    
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:34"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_4.png",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content="**\\*you think saw something running***"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Say: \"what was that?\"",
                    custom_id="what-was-that",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Say: \"i think i saw someone\"",
                    custom_id="i-think-i-saw someone",
                ),
        ),
    )


class Level_1_n5(discord.ui.LayoutView):  
  def __init__(self, user):
    super().__init__()    
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:35"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_5.png",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content=f"**{user}:** what was that?\n**John:** what?"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Say: \"forget about that, maybe it was the light\"",
                    custom_id="maybe-it-was-the-light",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Say: \"i think i saw someone\"",
                    custom_id="i-think-i-saw-someone",
                ),
        ),
    )
    self.add_item(container1)



class Level_1_n6(discord.ui.LayoutView):    
    def __init__(self, user):
        super().__init__()   
        container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:35"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_5.png",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content=f"**{user}:** i think i saw someone\n**John:** from the team?\n**Radio | John:** Thomas, Carl, can you hear me?\n**Radio: ** **\\*static***"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Continue walking",
                    custom_id="573ed2c54f374686c8beef2714381c8f",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Say: \"i think i saw someone\"",
                    disabled=True,
                    custom_id="a901ab7a10dc4a9398df20b2a2fd562d",
                ),
        ),
    )
        self.add_item(container1)

class Level_1_n7(discord.ui.LayoutView):    
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# - Recording <t:1791449160:t>"),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="https://i.imgur.com/ll6Lp64.jpeg",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="<--",
                    custom_id="button-left-level-1-n-8",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="You still have your sanity.",
                    disabled=True,
                    custom_id="button-drink-level-1",
                ),
        ),
    )    

class Level_1_n8(discord.ui.LayoutView):    
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# - Recording <t:1791448860:t>"),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="https://preview.redd.it/deep-hole-in-the-floor-v0-7ks2hy7vzoqc1.jpg?width=640&format=pjpg&auto=webp&s=2ca7490db650e42996f6d4a96a9f0598ad77a6a1",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Throw myself",
                    custom_id="button-level-1-exit",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="-->",
                    custom_id="button-right-level-1-n-7",
                ),
        ),
    )



@bot.event
async def on_ready():
   await bot.change_presence(status=discord.Status.idle, activity=discord.activity.CustomActivity("..."))


@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type != discord.InteractionType.component:
        return
    cid = interaction.data["custom_id"]
    if cid == "button-start2" or cid == "button-start":
        await interaction.response.send_message("Linking...", ephemeral=True)
        perms = interaction.channel.overwrites_for(interaction.user)
        perms.view_channel = False
        await interaction.channel.set_permissions(interaction.user, overwrite=perms)
        category_perms={interaction.user: discord.PermissionOverwrite(view_channel=True), interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        category_user=await interaction.guild.create_category(f"{interaction.user.display_name}",overwrites=category_perms)
        canal = await interaction.guild.create_text_channel(
            "level-01", category=category_user, overwrites=category_perms
        )
        await canal.send(view=Level_1_n1(), files=[discord.File("assets/screen_1.png")])
    elif cid == "button-how-long-until-we-leave":
        await interaction.response.edit_message(view=Level_1_n2(interaction.user.display_name), files=[discord.File("assets/screen_2.png")])
    elif cid == "button-continue-walking":
        await interaction.response.edit_message(view=Level_1_n3(), files=[discord.File("assets/screen_3.png")])
        await asyncio.sleep(2)
        await interaction.response.edit_message(view=Level_1_n4(), files=[discord.File("assets/screen_4.png")])
    elif cid == "what-was-that":
        await interaction.response.edit_message(view=Level_1_n5(interaction.user.display_name), files=[discord.File("assets/screen_5.png")])
    elif cid == "i-think-i-saw-someone":
        await interaction.response.edit_message(view=Level_1_n6(interaction.user.display_name), files=[discord.File("assets/screen_5.png")])

          



    elif cid == "button-level-1-exit":
        await interaction.channel.edit(name="l͓̦ͨ͑ͥe͑̓ͯv̩̞͒͐̌͆ḛ̗̻l̳ͬ-̗̄͛̃0̣̪̳̮ͬ̔ͨ1̉̆ͤ")
        await interaction.response.send_message("Linking...", ephemeral=True)
        category_perms={interaction.user: discord.PermissionOverwrite(view_channel=True), interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        category_user=interaction.channel.category
        time.sleep(2)
        canal = await interaction.guild.create_text_channel(
                    "level-02", category=category_user, overwrites=category_perms
                )
        #await canal.send(view=Level_2_n1())
        await interaction.channel.delete()








@bot.command()
async def lobby_send_container(ctx: commands.Context) -> None:
    if ctx.author.guild_permissions.administrator == True:
      await ctx.send(view=lobbycontainer())
      await ctx.message.delete()


bot.run(os.environ.get("DISCORDTOKEN"))