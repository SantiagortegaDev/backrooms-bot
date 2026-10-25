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
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="attachment://screen_17.webp")
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content="**Jonh:** I'm a bit tired, i think that's enough"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.ActionRow(
            discord.ui.Button(
                label="Continue walking",
                style=discord.ButtonStyle.secondary,
                custom_id="button-2-continue-walking"
            )
        )
    )    

class Level_1_n20(discord.ui.LayoutView):
        container1=discord.ui.Container(
            discord.ui.TextDisplay(content="# Recording 10:44"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.MediaGallery(
                discord.MediaGalleryItem(
                    media="attachment://screen_18.webp")
            ),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.TextDisplay(content="**\\*You see a door***"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.ActionRow(
                discord.ui.Button(
                    label="Say: \"Wait, look, a door\"",
                    style=discord.ButtonStyle.secondary,
                    custom_id="button-wait-a-door"
                ),
                discord.ui.Button(
                    label="Say: \"THE EXIT?!?\"",
                    style=discord.ButtonStyle.secondary,
                    custom_id="button-the-exit-fake-xd"
                )
            )
        )    

class Level_1_n21(discord.ui.LayoutView):
        def __init__(self, user):
         super().__init__()     
         container1=discord.ui.Container(
             discord.ui.TextDisplay(content="# Recording 10:44"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.MediaGallery(
                 discord.MediaGalleryItem(
                     media="attachment://screen_19.webp")
             ),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.TextDisplay(content=f"**@{user}:** THE EXIT?!?\n**Jonh:** let's hope so, let's see what's inside"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.ActionRow(
                 discord.ui.Button(
                     label="Look inside the door",
                     style=discord.ButtonStyle.secondary,
                     custom_id="inside-the-door"
                 ),
             )
         )    
         self.add_item(container1)

class Level_1_n22(discord.ui.LayoutView):
        def __init__(self, user):
         super().__init__()    
         container1=discord.ui.Container(
             discord.ui.TextDisplay(content="# Recording 10:46"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.MediaGallery(
                 discord.MediaGalleryItem(
                     media="attachment://screen_19.webp")
             ),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.TextDisplay(content=f"**@{user}:** wait, look, a door\n**Jonh:** what's inside?"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.ActionRow(
                 discord.ui.Button(
                     label="Look inside the door",
                     style=discord.ButtonStyle.secondary,
                     custom_id="inside-the-door"
                 ),
             )
         )    
         self.add_item(container1)

class Level_1_n23(discord.ui.LayoutView):
        container1=discord.ui.Container(
            discord.ui.TextDisplay(content="# Recording 10:47"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.MediaGallery(
                discord.MediaGalleryItem(
                    media="attachment://screen_20.webp")
            ),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.ActionRow(
                discord.ui.Button(
                    label="\u200b",
                    style=discord.ButtonStyle.secondary,
                    custom_id="fejwkhfjkewjfhew",
                    disabled=True
                ),
            )
        )    

class Level_1_n24(discord.ui.LayoutView):
        def __init__(self, user):
         super().__init__()
         container1=discord.ui.Container(
             discord.ui.TextDisplay(content="# Recording 10:48"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.MediaGallery(
                 discord.MediaGalleryItem(
                     media="attachment://screen_21.webp")
             ),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.TextDisplay(content=f"**@{user}:** well, another hallway"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.ActionRow(
                 discord.ui.Button(
                     label="Say: \"what's exactly this place?\"",
                     style=discord.ButtonStyle.secondary,
                     custom_id="whats-this-place"
                 ),
                 discord.ui.Button(
                     label="Say: \"who pays the electricity bill?\"",
                     style=discord.ButtonStyle.secondary,
                     custom_id="who-pays-electricity"
                 )
             )
         )    
         self.add_item(container1)    

class Level_1_n25(discord.ui.LayoutView):
        container1=discord.ui.Container(
            discord.ui.TextDisplay(content="# Recording 10:49"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.MediaGallery(
                discord.MediaGalleryItem(
                    media="attachment://screen_22.webp")
            ),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.TextDisplay(content="**\\*You hear the door close***"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.ActionRow(
                discord.ui.Button(
                    label="Turn my head",
                    style=discord.ButtonStyle.secondary,
                    custom_id="turn-my-head"
                ),
                discord.ui.Button(
                    label="Say: \"Jonh tell me that you close the door\"",
                    style=discord.ButtonStyle.secondary,
                    custom_id="jonh-tell-close-door"
                )
            )
        )


class Level_1_n26(discord.ui.LayoutView):
        def __init__(self, user):
         super().__init__()
         container1=discord.ui.Container(
             discord.ui.TextDisplay(content="# Recording 10:50"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.MediaGallery(
                 discord.MediaGalleryItem(
                     media="attachment://screen_23.webp")
             ),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.TextDisplay(content=f"**@{user}:** jonh tell me that you closes the door\n**Jonh:** no, i didn't close it"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.ActionRow(
                 discord.ui.Button(
                     label="Turn my head",
                     style=discord.ButtonStyle.secondary,
                     custom_id="turn-my-head"
                 ),
                 discord.ui.Button(
                     label="Say: \"Jonh tell me that you close the door\"",
                     style=discord.ButtonStyle.secondary,
                     custom_id="jonh-tell-close-door",
                     disabled=True
                 )
             )
         )
         self.add_item(container1)

class Level_1_n27(discord.ui.LayoutView):
         container1=discord.ui.Container(
             discord.ui.TextDisplay(content="# Recording 10:51"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.MediaGallery(
                 discord.MediaGalleryItem(
                     media="attachment://screen_24.webp")
             ),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.ActionRow(
                 discord.ui.Button(
                     label="Check if the door opens",
                     style=discord.ButtonStyle.secondary,
                     custom_id="check-the-door"
                 )
             )
         )

class Level_1_n28(discord.ui.LayoutView):
         container1=discord.ui.Container(
             discord.ui.TextDisplay(content="# Recording 10:52"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.MediaGallery(
                 discord.MediaGalleryItem(
                     media="attachment://screen_25.webp")
             ),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.ActionRow(
                 discord.ui.Button(
                     label="\u200b",
                     style=discord.ButtonStyle.secondary,
                     custom_id="dfjkdshfjksdkf",
                     disabled=True
                 )
             )
         )

class Level_1_n29(discord.ui.LayoutView):
         container1=discord.ui.Container(
             discord.ui.TextDisplay(content="# Recording 10:52"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.MediaGallery(
                 discord.MediaGalleryItem(
                     media="attachment://screen_26.webp")
             ),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.TextDisplay(content="**\\*The door didn't open***"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.ActionRow(
                 discord.ui.Button(
                     label="Say: \"what do we do now?\"",
                     style=discord.ButtonStyle.secondary,
                     custom_id="what-do-we-do-now"
                 ),
                 discord.ui.Button(
                      label="Try again",
                      style=discord.ButtonStyle.secondary,
                      custom_id="try-again"
                 )
             )
         )

class Level_1_n30(discord.ui.LayoutView):
         container1=discord.ui.Container(
             discord.ui.TextDisplay(content="# Recording 10:53"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.MediaGallery(
                 discord.MediaGalleryItem(
                     media="attachment://screen_26.webp")
             ),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.TextDisplay(content="**\\*The door is still locked***"),
             discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
             discord.ui.ActionRow(
                 discord.ui.Button(
                     label="Say: \"what do we do now?\"",
                     style=discord.ButtonStyle.secondary,
                     custom_id="what-do-we-do-now"
                 ),
                 discord.ui.Button(
                      label="Try again",
                      style=discord.ButtonStyle.secondary,
                      custom_id="try-again",
                      disabled=True
                 )
             )
         )

class Level_1_n31(discord.ui.LayoutView):
         def __init__(self, user):
          super().__init__()
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:54"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_27.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.TextDisplay(content=f"**@{user}:** what do we do now? we can't go back\n**Jonh:** let's continue we need to leave"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="Continue walking",
                      style=discord.ButtonStyle.secondary,
                      custom_id="continue-walking-3-i-think"
                  )
              )
          )
          self.add_item(container1)

class Level_1_n32(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:55"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_28.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.TextDisplay(content="**Jonh:** also, we are not authorized to answer those questions"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="Continue walking",
                      style=discord.ButtonStyle.secondary,
                      custom_id="continue-4-walking"
                  )
              )
          )

class Level_1_n33(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:55"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_29.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="jjdfsjfksdf",
                      disabled=True
                  )
              )
          )          

class Level_1_n34(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:56"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_30.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="mjweknfjksd",
                      disabled=True
                  )
              )
          )

class Level_1_n35(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:56"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_31.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.TextDisplay(content="**Jonh:** you're crazy if you think i'm going to keep going that way"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="Say: \"well, it's the only option\"",
                      style=discord.ButtonStyle.secondary,
                      custom_id="only-option"
                  ),
                  discord.ui.Button(
                    label="Say: \"and what do you propose?\"",
                    style=discord.ButtonStyle.secondary,
                    custom_id="what-do-you-proporse"
                )
              )
          )

class Level_1_n36(discord.ui.LayoutView):
        def __init__(self, user):
          super().__init__()
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:58"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_32.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.TextDisplay(content=f"**@{user}:** well, it's the only option\n**Jonh:** well, you're right about that, but i'm not going that way"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="Continue walking",
                      style=discord.ButtonStyle.secondary,
                      custom_id="continue-walking-555"
                  )
              )
          )           
          self.add_item(container1)

class Level_1_n37(discord.ui.LayoutView):
        def __init__(self, user):
          super().__init__()
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:58"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_32.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.TextDisplay(content=f"**@{user}:** and what do you propose?\n**Jonh:** nothing, if you want continue, but i'm not going that way"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="Continue walking",
                      style=discord.ButtonStyle.secondary,
                      custom_id="continue-walking-555"
                  )
              )
          )           
          self.add_item(container1)

class Level_1_n38(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:59"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_33.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="ueasdhfuikewf",
                      disabled=True
                  )
              )
          )           

       
class Level_1_n39(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:59"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_34.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="nsdjkfhsdukfsd",
                      disabled=True
                  )
              )
          )       

class Level_1_n40(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:59"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_35.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="jsuofsjdlfsldfsd",
                      disabled=True
                  )
              )
          )       


class Level_1_n41(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:59"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_36.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.TextDisplay(content="**Jonh:** ok, ok, i will going with you, we must not separate"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="Continue walking",
                      style=discord.ButtonStyle.secondary,
                      custom_id="continue-walking-11"
                  )
              )
          )       

class Level_1_n42(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 10:59"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_37.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="njkfsdhbkfhsdkuf",
                      disabled=True
                  )
              )
          )       

class Level_1_n43(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 11:00"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_38.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="njkfsdhbkfhsdkuf",
                      disabled=True
                  )
              )
          )       

class Level_1_n44(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 11:00"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_39.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="fnjdskfkjdsffdfsr",
                      disabled=True
                  )
              )
          )       

class Level_1_n45(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 11:00"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_40.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="sdjiuofhdsukfsd",
                      disabled=True
                  )
              )
          )       

class Level_1_n46(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 11:00"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_41.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="gnjkfgnjkfsnjfsd",
                      disabled=True
                  )
              )
          )       


class Level_1_n47(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Recording 11:00"),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.MediaGallery(
                  discord.MediaGalleryItem(
                      media="attachment://screen_42.webp")
              ),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.ActionRow(
                  discord.ui.Button(
                      label="\u200b",
                      style=discord.ButtonStyle.secondary,
                      custom_id="juifsdhukfhsdukfsdku",
                      disabled=True
                  )
              )
          )       


class Level_1_n48(discord.ui.LayoutView):
          container1=discord.ui.Container(
              discord.ui.TextDisplay(content="# Stoping recording..."),
              discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
              discord.ui.TextDisplay(content="Unlinking...")
          )       

class lastmessage(discord.ui.LayoutView):    
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="Thank you for supporting the neural data collection program\nFor more details visit: [hͥͤtt̬̽p̫͗ͧ:͚/̎ͤ/ͬ̏b̃͒a͇͗̇c̬ḵ̂̑r̝͐̏ǒ̻õm̦̅̃s͑.͙̥ͫl̹̜o͕̭̊c͓͋̿aͨlͥ̐/͍̫ͦṉe̲̠ͤ̇u̯ra͍̱ͤl̠̽́-̣͉ͦp͔͇rͬ̉ọg̝̳͆ra̺m̲̅](https://hackclub.com/backrooms-neural-program-hmmm-it-seems-that-hack-club-want-to-hide-this-information)\n-# Backrooms organization."),
    )
    
    container2 = discord.ui.Container(
        discord.ui.TextDisplay(content="**Hey, santiago here!**"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
        discord.ui.TextDisplay(content="I hope you enjoy playing this little game\naaaaaand i would love to hear what you thought of it\n(pls don't ignore me)"),
        discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.secondary,
                    label="Send a message",
                    custom_id="send-message-button",
                ),
        ),
        discord.ui.TextDisplay(content="**Thanks for playing!!**"),
    )
    container3 = discord.ui.Container(
         discord.ui.ActionRow(
              discord.ui.Button(
                   style=discord.ButtonStyle.secondary,
                   label="Play again",
                   custom_id="play-again-finally-you-did-it"
              )
         )
    )

class messagemodal(discord.ui.Modal, title="Send me a message"):
    msg = discord.ui.TextInput(label="Message:", style=discord.TextStyle.long, required=True, placeholder="wow, that was the best game i ever played in almost 15 years...")

    async def on_submit(self, interaction: discord.Interaction):
        channel_msg = await bot.fetch_channel(1563329164625318038)
        await channel_msg.send(f"**{interaction.user.display_name}:** {self.msg}")
        await interaction.response.send_message(f"Thanks!", ephemeral=True)


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
        await interaction.delete_original_response()
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
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n19(), attachments=[discord.File("assets/screen_17.webp")])

    elif cid == "button-2-continue-walking":
         await interaction.response.defer()
         await interaction.edit_original_response(view=Level_1_n20(), attachments=[discord.File("assets/screen_18.webp")])

    elif cid == "button-wait-a-door":
         await interaction.response.defer()
         await interaction.edit_original_response(view=Level_1_n22(interaction.user.display_name), attachments=[discord.File("assets/screen_19.webp")])
    elif cid == "button-the-exit-fake-xd":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n21(interaction.user.display_name), attachments=[discord.File("assets/screen_19.webp")])
    elif cid == "inside-the-door":
         await interaction.response.defer()
         message = interaction.message
         await interaction.edit_original_response(view=Level_1_n23(), attachments=[discord.File("assets/screen_20.webp")])
         await asyncio.sleep(2)
         await message.edit(view=Level_1_n24(interaction.user.display_name), attachments=[discord.File("assets/screen_21.webp")])
    elif cid == "who-pays-electricity" or cid == "whats-this-place":
         await interaction.response.defer()
         await interaction.edit_original_response(view=Level_1_n25(), attachments=[discord.File("assets/screen_22.webp")])
    elif cid == "jonh-tell-close-door":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n26(interaction.user.display_name), attachments=[discord.File("assets/screen_23.webp")])
    elif cid == "turn-my-head":
         await interaction.response.defer()
         await interaction.edit_original_response(view=Level_1_n27(), attachments=[discord.File("assets/screen_24.webp")])
    elif cid == "check-the-door":
         message = interaction.message
         await interaction.response.defer()
         await interaction.edit_original_response(view=Level_1_n28(), attachments=[discord.File("assets/screen_25.webp")])
         await asyncio.sleep(1.5)
         await message.edit(view=Level_1_n29(), attachments=[discord.File("assets/screen_26.webp")])
    elif cid == "what-do-we-do-now":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n31(interaction.user.display_name), attachments=[discord.File("assets/screen_27.webp")])   
    elif cid == "try-again":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n30(), attachments=[discord.File("assets/screen_26.webp")])      
    elif cid == "continue-walking-3-i-think":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n32(),attachments=[discord.File("assets/screen_28.webp")])
    elif cid == "continue-4-walking":
         await interaction.response.defer()
         await interaction.edit_original_response(view=Level_1_n33(), attachments=[discord.File("assets/screen_29.webp")])
         message = interaction.message
         await asyncio.sleep(1.5)
         await message.edit(view=Level_1_n34(), attachments=[discord.File("assets/screen_30.webp")])   
         await asyncio.sleep(1.5)
         await message.edit(view=Level_1_n35(), attachments=[discord.File("assets/screen_31.webp")])
    elif cid == "only-option":
         await interaction.response.defer()
         await interaction.edit_original_response(view=Level_1_n36(interaction.user.display_name), attachments=[discord.File("assets/screen_32.webp")])
    elif cid == "what-do-you-proporse":
        await interaction.response.defer()
        await interaction.edit_original_response(view=Level_1_n37(interaction.user.display_name), attachments=[discord.File("assets/screen_32.webp")])
    elif cid == "continue-walking-555":
        await interaction.response.defer()
        message = interaction.message
        await interaction.edit_original_response(view=Level_1_n38(), attachments=[discord.File("assets/screen_33.webp")])
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n39(), attachments=[discord.File("assets/screen_34.webp")])
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n40(), attachments=[discord.File("assets/screen_35.webp")])
        await asyncio.sleep(1.5)
        await message.edit(view=Level_1_n41(), attachments=[discord.File("assets/screen_36.webp")])

    elif cid == "continue-walking-11":
         await interaction.response.defer()
         message = interaction.message
         await interaction.edit_original_response(view=Level_1_n42(), attachments=[discord.File("assets/screen_37.webp")])
         await asyncio.sleep(1.5)
         await message.edit(view=Level_1_n43(), attachments=[discord.File("assets/screen_38.webp")])
         await asyncio.sleep(1.5)
         await message.edit(view=Level_1_n44(), attachments=[discord.File("assets/screen_39.webp")])
         await asyncio.sleep(1.5)
         await message.edit(view=Level_1_n45(), attachments=[discord.File("assets/screen_40.webp")])         
         await asyncio.sleep(1.5)
         await message.edit(view=Level_1_n46(), attachments=[discord.File("assets/screen_41.webp")])         
         await asyncio.sleep(1.5)
         await message.edit(view=Level_1_n47(), attachments=[discord.File("assets/screen_42.webp")])
         await interaction.channel.edit(name="l͓̦ͨ͑ͥe͑̓ͯv̩̞͒͐̌͆ḛ̗̻l̳ͬ-̗̄͛̃0̣̪̳̮ͬ̔ͨ1̉̆ͤ")
         await asyncio.sleep(2)
         await message.edit(view=Level_1_n48())
         category_perms={interaction.user: discord.PermissionOverwrite(view_channel=True), interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False)}
         category_user=interaction.channel.category
         await asyncio.sleep(1.5)
         channel2 = await interaction.guild.create_text_channel(
                     "the-end", category=category_user, overwrites=category_perms
                 )
         await channel2.send(view=lastmessage())
         await interaction.channel.delete()
    elif cid == "send-message-button":
         await interaction.response.send_modal(messagemodal())
    elif cid == "play-again-finally-you-did-it":
         await interaction.channel.delete()
         await interaction.channel.category.delete()
         channel = interaction.guild.get_channel(1557387255335882892)
         await channel.set_permissions(interaction.user, overwrite=None) 




    #hey!, easter egg, i originaly plan to be like levels, like level 1-2-3, 
    #but i realize that there aren't a lot of pictures of the pool rooms for example, 
    #anyways i like the path i choose, here is the lore, only for the people that read this

    #lore: you enter a neural data collection program of the backrooms org, that's the why are messages like linking...
    #hackclub supports this program but it's private, some people has been found in the streets without last 
    #memories and with 500 dolars in their pocket, so no one make questions
    #you never enter the backrooms, your brain enter the backrooms, the alpha neurochip is the device you use 
    #yeah, i know, i create this lore 3 minutes ago but it's cool xd
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