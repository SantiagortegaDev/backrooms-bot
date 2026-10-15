import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import time
import asyncio
from datetime import datetime

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
        discord.ui.TextDisplay(content=f"# Recording 10:30"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_1.webp",
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
        discord.ui.TextDisplay(content="# Recording 10:32"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_2.webp",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content=f"**@{user}:** how long until we leave?\n**John:** we're about to reach Sector 7 **\\*sigh*** it won't be long now."),
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
                media="attachment://screen_3_1.webp",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="\u200b",
                    disabled=True,
                    custom_id="573ed2c54f374686c8beef2714381c8f",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="\u200b",
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
                media="attachment://screen_4.webp",
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
                    custom_id="i-think-i-saw-someone",
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
                media="attachment://screen_5.webp",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content=f"**@{user}:** what was that?\n**John:** what?"),
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


class Level_1_n10(discord.ui.LayoutView):
    def __init__(self, user):
        super().__init__()
        container1= discord.ui.Container(
            discord.ui.TextDisplay(content="# Recording 10:36"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.MediaGallery(
                discord.MediaGalleryItem(media="attachment://screen_6.webp"
                )
            ),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.TextDisplay(content=f"**@{user}:** ok, let's continue"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.ActionRow(
                discord.ui.Button(style=discord.ButtonStyle.secondary,label="Continue walking", custom_id="button-continue-walking-2"),
                discord.ui.Button(style=discord.ButtonStyle.secondary,label="Say: \"forget about that, maybe it was the light\"", disabled=True, custom_id="gjirfjgrjgureger")
            )

        )
        self.add_item(container1)




class Level_1_n6(discord.ui.LayoutView):    
    def __init__(self, user):
        super().__init__()   
        container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:36"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_6.webp",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content=f"**@{user}:** i think i saw someone\n**John:** from the team?\n**Radio | John:** Thomas, Carl, can you hear me?\n**Radio: ** **\\*static***"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Continue walking",
                    custom_id="button-continue-walking-2",
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
        discord.ui.TextDisplay(content="# Recording 10:37"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_7.webp",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="\u200b",
                    disabled=True,
                    custom_id="573ed2c54f374686c8beef2714381c8f",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="\u200b",
                    disabled=True,
                    custom_id="a901ab7a10dc4a9398df20b2a2fd562d",
                ),
        ),
    )

class Level_1_n8(discord.ui.LayoutView):    
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:38"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_8.webp",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="\u200b",
                    disabled=True,
                    custom_id="573ed2c54f374686c8beef2714381c8f",
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="\u200b",
                    disabled=True,
                    custom_id="a901ab7a10dc4a9398df20b2a2fd562d",
                ),
        ),
    )

class Level_1_n9(discord.ui.LayoutView):
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:38"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(discord.MediaGalleryItem(media="attachment://screen_9.webp"),),
        discord.ui.Separator(visible=True,spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content="**Jonh:** Oh no"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(discord.ui.Button(style=discord.ButtonStyle.secondary,label='Say: "is this supposed to be like this?"',custom_id="is-this-supposed-to-be-like-this"),discord.ui.Button(style=discord.ButtonStyle.secondary,label='Shout: "HELP!"',custom_id="button-shout-help"))
        )

class Level_1_n11(discord.ui.LayoutView):
    def __init__(self, user):
      super().__init__()
      container1=discord.ui.Container(
          discord.ui.TextDisplay(content="# Recording 10:39"),
          discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
          discord.ui.MediaGallery(
              discord.MediaGalleryItem(
                  media="attachment://screen_10.webp"
              )
          ),
          discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
          discord.ui.TextDisplay(content=f"**@{user}:** is this supposed to be like this?\n**Jonh:** Of course it shouldn't be like this, let me call the supervisor\n**Radio:** **\\*static***\n**John:** Well i will let you choose the path"),
          discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
          discord.ui.TextDisplay(content="**Let me choose:**"),
          discord.ui.ActionRow(
              discord.ui.Button(
                  style=discord.ButtonStyle.secondary,
                  label="▓▓",
                  custom_id="choose-path-1"
              ),
              discord.ui.Button(
                  style=discord.ButtonStyle.secondary,
                  label="▓▓",
                  custom_id="choose-path-2"
              ),
              discord.ui.Button(
                  style=discord.ButtonStyle.secondary,
                  label="▓▓",
                  custom_id="choose-path-3"
              ),
              discord.ui.Button(
                  style=discord.ButtonStyle.secondary,
                  label="▓▓",
                  custom_id="choose-path-4"
              )
          )
      )
      self.add_item(container1)

class Level_1_n12(discord.ui.LayoutView):
    def __init__(self,user):
        super().__init__()
        container1=discord.ui.Container(
            discord.ui.TextDisplay(content="# Recording 10:39"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.MediaGallery(
                discord.MediaGalleryItem(
                    media="attachment://screen_11.webp"
                )
            ),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.TextDisplay(content=f"**@{user}:** HELP!\n**Jonh:** no one is going to listen you\n**Radio:** **\\*static***\n**Jonh:** well, the radio don't have signal, choose a path to continue"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.TextDisplay(content="**Let me choose:**"),
            discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="▓▓",
                    custom_id="choose-path-1"
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="▓▓",
                    custom_id="choose-path-2"
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="▓▓",
                    custom_id="choose-path-3"
                ),
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="▓▓",
                    custom_id="choose-path-4"
                )
            )
        )      
        self.add_item(container1)

class Level_1_n13(discord.ui.LayoutView):
    def __init__(self, user):
        super().__init__()
        container1=discord.ui.Container(
            discord.ui.TextDisplay(content="# Recording 10:40"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.MediaGallery(
                discord.MediaGalleryItem(
                    media="attachment://screen_12.webp"
                )
            ),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.TextDisplay(content=f"**Jonh:** ok, let's g.. wait *\\*starts whispering** \n-# i think i listen something"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="RUN",
                    custom_id="button-run"
                )
            )
        )
        self.add_item(container1)

class Level_1_n14(discord.ui.LayoutView):
        container1=discord.ui.Container(
            discord.ui.TextDisplay(content="# Recording 10:41"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.MediaGallery(
                discord.MediaGalleryItem(
                    media="attachment://screen_13.webp"
                )
            ),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="\u200b",
                    custom_id="njjfsjdoidjfsodsds",
                    disabled=True
                )
            )
        )

class Level_1_n15(discord.ui.LayoutView):
    container1=discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:41"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_14.webp"
            )
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
            discord.ui.Button(
                style=discord.ButtonStyle.secondary,
                label="\u200b",
                custom_id="fnsuehfukwhfulqe",
                disabled=True
            )
        )
    )        

class Level_1_n16(discord.ui.LayoutView):
    container1=discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:41"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_15.webp"
            )
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
            discord.ui.Button(
                style=discord.ButtonStyle.secondary,
                label="\u200b",
                custom_id="nrsnfglwefleqfjlw",
                disabled=True
            )
        )
    )

class Level_1_n17(discord.ui.LayoutView):
    container=discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:41"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_16.webp"
            )
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
            discord.ui.Button(
                style=discord.ButtonStyle.secondary,
                label="\u200b",
                custom_id="vnjdsnfljajfilael",
                disabled=True
            )
        )
    )

class Level_1_n18(discord.ui.LayoutView):
    container1=discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:33"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(media="attachment://screen_3.webp")
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
            discord.ui.Button(
                style=discord.ButtonStyle.secondary,
                label="\u200b",
                custom_id="fnjkdsnfgljflkk",
                disabled=True
            ),
            discord.ui.Button(
                style=discord.ButtonStyle.secondary,
                label="\u200b",
                custom_id="fjkeafjlaejfliaejl",
                disabled=True
            )
        )
    )


class Level_1_n19(discord.ui.LayoutView):
    container1=discord.ui.Container(
        discord.ui.TextDisplay(content="# Recording 10:43"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small)
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
        await canal.send(view=Level_1_n1(), files=[discord.File("assets/screen_1.webp")])
    elif cid == "button-how-long-until-we-leave":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n2(interaction.user.display_name), attachments=[discord.File("assets/screen_2.webp")])
    elif cid == "button-continue-walking":
        await interaction.response.defer()
        message=interaction.message
        await interaction.edit_original_response(view=Level_1_n3(), attachments=[discord.File("assets/screen_3_1.webp")])
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n18(), attachments=[discord.File("assets/screen_3.webp")])
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n4(), attachments=[discord.File("assets/screen_4.webp")])
    elif cid == "what-was-that":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n5(interaction.user.display_name), attachments=[discord.File("assets/screen_5.webp")])
    elif cid == "i-think-i-saw-someone":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n6(interaction.user.display_name), attachments=[discord.File("assets/screen_6.webp")])
    elif cid == "button-continue-walking-2":
        await interaction.response.defer()
        message= interaction.message
        await interaction.edit_original_response(view=Level_1_n7(), attachments=[discord.File("assets/screen_7.webp")])
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n8(), attachments=[discord.File("assets/screen_8.webp")])
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n9(), attachments=[discord.File("assets/screen_9.webp")])
    elif cid == "maybe-it-was-the-light":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n10(interaction.user.display_name), attachments=[discord.File("assets/screen_6.webp")])
    elif cid == "is-this-supposed-to-be-like-this":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n11(interaction.user.display_name), attachments=[discord.File("assets/screen_10.webp")])
    elif cid == "button-shout-help":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n12(interaction.user.display_name), attachments=[discord.File("assets/screen_11.webp")])
    elif cid == "choose-path-1" or cid == "choose-path-2" or cid == "choose-path-3" or cid == "choose-path-4":
        await interaction.response.defer()
        message=interaction.message
        await interaction.edit_original_response(view=Level_1_n13(interaction.user.display_name), attachments=[discord.File("assets/screen_12.webp")])
        
    elif cid == "button-run":
        await interaction.response.defer()
        message=interaction.message
        await interaction.edit_original_response(view=Level_1_n14(), attachments=[discord.File("assets/screen_13.webp")])
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n15(), attachments=[discord.File("assets/screen_14.webp")])
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n16(), attachments=[discord.File("assets/screen_15.webp")])
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n17(), attachments=[discord.File("assets/screen_16.webp")])



    elif cid == "button-level-1-exit":
        await interaction.response.defer()
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