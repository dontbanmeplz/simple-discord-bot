import interactions
from datetime import datetime, timedelta
import datetime as dt
import utils
js = utils.js("db.json")
bot = interactions.Client(token="OTc3MjQ0MjYzNzAyMjI0OTI3.Gc3ePh.8QYCAk41dMqJ03B3i1WliJ9SAn7k-Ddgp5V-6o", disable_sync=False)
def funcc(e):
    return e["pos"]
def datepar(im):
    if im.endswith("s"):
        dt = datetime.now()
        td = timedelta(seconds=int(im[:-1]))
    elif im.endswith("m"):
        dt = datetime.now()
        td = timedelta(minutes=int(im[:-1]))
    elif im.endswith("h"):
        dt = datetime.now()
        td = timedelta(hours=int(im[:-1]))
    elif im.endswith("w"):
        dt = datetime.now()
        td = timedelta(weeks=int(im[:-1]))
    else:
        return False
    return dt + td

@bot.command(
    name="ban",
    description="Ban Someone",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.BAN_MEMBERS,
    options=[interactions.Option(
                    name="user",
                    description="user to ban",
                    type=interactions.OptionType.USER,
                    required=True,
    ),
    interactions.Option(
                    name="reason",
                    description="reason of ban",
                    type=interactions.OptionType.STRING,
                    required=False,
    )]
)
async def ban(ctx: interactions.CommandContext, user, reason = None):
    await ctx.get_guild()
    #user = interactions.User(**await bot._http.get_user(int(user)))
    id = int(user.user.id)
    if id == 977244263702224927:
        return await ctx.send("You cannot ban this bot")
    elif id == int(ctx.author.user.id):
        return await ctx.send("You cannot ban yourself")
    bb = await ctx.guild.get_member(int(bot.me.id))
    if user.roles == None:
        r = 0
    else:
        use = []
        for i in ctx.guild.roles:
            if int(i.id) in user.roles:
                use.append({"pos": i.position, "role": i})
        use.sort(key=funcc, reverse=True)
        r = use[0]["pos"]
    if ctx.author.roles == None:
        r2 = 0
    else:
        sel = []
        for i in ctx.guild.roles:
            if int(i.id) in ctx.author.roles:
                sel.append({"pos": i.position, "role": i})
        sel.sort(key=funcc, reverse=True)
        r2 = sel[0]["pos"]
    if bb.roles == 0:
        r3 = 0
    else:
        bo = []
        for i in ctx.guild.roles:
            if int(i.id) in bb.roles:
                bo.append({"pos": i.position, "role": i})
        bo.sort(key=funcc, reverse=True)
    #r = use[0]["pos"]
    #r2 = sel[0]["pos"]
    r3 = bo[0]["pos"]
    if r3<r:
        return await ctx.send("I do not have enough permissions to ban this person")
    if r2 > r or ctx.guild.owner_id == ctx.author.user.id:
        if reason == None:
            reason = "banned"
        await user.ban(ctx.guild_id, reason=reason)
    else:
        return await ctx.send("You cannot ban someone higher than yourself")
    await ctx.send(f"{user.user.username} has been baned")

@bot.command(
    name="kick",
    description="Kick Someone",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.KICK_MEMBERS,
    options=[interactions.Option(
                    name="user",
                    description="user to kick",
                    type=interactions.OptionType.USER,
                    required=True,
    ),
    interactions.Option(
                    name="reason",
                    description="reason of kick",
                    type=interactions.OptionType.STRING,
                    required=False,
    )]
)
async def kick(ctx: interactions.CommandContext, user, reason = None):
    await ctx.get_guild()
    #user = interactions.User(**await bot._http.get_user(int(user)))
    id = int(user.user.id)
    if id == 977244263702224927:
        return await ctx.send("You cannot kick this bot")
    elif id == int(ctx.author.user.id):
        return await ctx.send("You cannot kick yourself")
    bb = await ctx.guild.get_member(int(bot.me.id))
    if user.roles == None:
        r = 0
    else:
        use = []
        for i in ctx.guild.roles:
            if int(i.id) in user.roles:
                use.append({"pos": i.position, "role": i})
        use.sort(key=funcc, reverse=True)
        r = use[0]["pos"]
    if ctx.author.roles == None:
        r2 = 0
    else:
        sel = []
        for i in ctx.guild.roles:
            if int(i.id) in ctx.author.roles:
                sel.append({"pos": i.position, "role": i})
        sel.sort(key=funcc, reverse=True)
        r2 = sel[0]["pos"]
    if bb.roles == 0:
        r3 = 0
    else:
        bo = []
        for i in ctx.guild.roles:
            if int(i.id) in bb.roles:
                bo.append({"pos": i.position, "role": i})
        bo.sort(key=funcc, reverse=True)
    #r = use[0]["pos"]
    #r2 = sel[0]["pos"]
    r3 = bo[0]["pos"]
    if r3<r:
        return await ctx.send("I do not have enough permissions to kick this person")
    if r2 > r or ctx.guild.owner_id == ctx.author.user.id:
        if reason == None:
            reason = "kicked"
        await user.kick(ctx.guild_id, reason=reason)
    else:
        return await ctx.send("You cannot kick someone higher than yourself")
    await ctx.send(f"{user.user.username} has been kicked")

@bot.command(
    name="purge",
    description="purge a channel",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.MANAGE_CHANNELS,
    options=[interactions.Option(
                    name="channel",
                    description="channel to purge",
                    type=interactions.OptionType.CHANNEL,
                    required=False,
    )])
async def purge(ctx, channel=None):
    await ctx.get_guild()
    if channel == None:
        await ctx.get_channel()
        c = ctx.channel
        js = ctx.channel._json
    else:
        c = interactions.Channel(**await bot._http.get_channel(channel.id), _client=bot._http)
        js = c._json
    js["permission_overwrites"] = [interactions.Overwrite(**_) for _ in js['permission_overwrites']]
    js.pop("id")
    js.pop("_client")
    js.pop("last_message_id")
    js.pop("flags")
    js.pop("guild_id")
    await c.delete()
    await ctx.guild.create_channel(**js)
    await ctx.send("Channel has been purged")

@bot.command(
    name="mute",
    description="Mute Someone",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.MODERATE_MEMBERS,
    options=[interactions.Option(
                    name="user",
                    description="user to mute",
                    type=interactions.OptionType.USER,
                    required=True,
    ), 
    interactions.Option(
                    name="time",
                    description="time to mute",
                    type=interactions.OptionType.STRING,
                    required=True,
    )])
async def mute(ctx,user, time):
    await ctx.get_guild()
    dt = datetime.now()
    
    td = timedelta(days=28)
    t = datepar(time)
    
    if t:
        pass
    else:
        return await ctx.send(f"{time} is not the valid format")
    if dt+td < t:
        return await ctx.send("You cannot mute for over 28 days")
    id = int(user.user.id)
    if id == 977244263702224927:
        return await ctx.send("You cannot mute this bot")
    elif id == int(ctx.author.user.id):
        return await ctx.send("You cannot mute yourself")
    bb = await ctx.guild.get_member(int(bot.me.id))
    if user.roles == None:
        r = 0
    else:
        use = []
        for i in ctx.guild.roles:
            if int(i.id) in user.roles:
                use.append({"pos": i.position, "role": i})
        use.sort(key=funcc, reverse=True)
        r = use[0]["pos"]
    if ctx.author.roles == None:
        r2 = 0
    else:
        sel = []
        for i in ctx.guild.roles:
            if int(i.id) in ctx.author.roles:
                sel.append({"pos": i.position, "role": i})
        sel.sort(key=funcc, reverse=True)
        r2 = sel[0]["pos"]
    if bb.roles == 0:
        r3 = 0
    else:
        bo = []
        for i in ctx.guild.roles:
            if int(i.id) in bb.roles:
                bo.append({"pos": i.position, "role": i})
        bo.sort(key=funcc, reverse=True)
    #r = use[0]["pos"]
    #r2 = sel[0]["pos"]
    r3 = bo[0]["pos"]
    if r3<r:
        return await ctx.send("I do not have enough permissions to mute this person")
    if r2 > r:
        if reason:
            pass
        else:
            reason = "Muted"
        
        await user.modify(
            ctx.guild_id, communication_disabled_until=t.isoformat(), reason=reason
        )
    else:
        return await ctx.send("You cannot mute someone higher than yourself")
    await ctx.send(f"{user.user.username} has been muted for {time}")

@bot.command(
    name="unmute",
    description="Unmute Someone",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.MODERATE_MEMBERS,
    options=[interactions.Option(
                    name="user",
                    description="user to unmute",
                    type=interactions.OptionType.USER,
                    required=True,
    )])
async def unmute(ctx,user):
    await ctx.get_guild()
    id = int(user.user.id)
    if id == 977244263702224927:
        return await ctx.send("You cannot unmute this bot")
    elif id == int(ctx.author.user.id):
        return await ctx.send("You cannot unmute yourself")
    bb = await ctx.guild.get_member(int(bot.me.id))
    if user.roles == None:
        r = 0
    else:
        use = []
        for i in ctx.guild.roles:
            if int(i.id) in user.roles:
                use.append({"pos": i.position, "role": i})
        use.sort(key=funcc, reverse=True)
        r = use[0]["pos"]
    if ctx.author.roles == None:
        r2 = 0
    else:
        sel = []
        for i in ctx.guild.roles:
            if int(i.id) in ctx.author.roles:
                sel.append({"pos": i.position, "role": i})
        sel.sort(key=funcc, reverse=True)
        r2 = sel[0]["pos"]
    if bb.roles == 0:
        r3 = 0
    else:
        bo = []
        for i in ctx.guild.roles:
            if int(i.id) in bb.roles:
                bo.append({"pos": i.position, "role": i})
        bo.sort(key=funcc, reverse=True)
    #r = use[0]["pos"]
    #r2 = sel[0]["pos"]
    r3 = bo[0]["pos"]
    if r3<r:
        return await ctx.send("I do not have enough permissions to unmute this person")
    if r2 > r:
        if reason:
            pass
        else:
            reason = "Muted"
        
        await user.modify(
            ctx.guild_id, communication_disabled_until=None, reason=reason
        )
    else:
        return await ctx.send("You cannot unmute someone higher than yourself")
    await ctx.send(f"{user.user.username} has been unmuted")

@bot.command(
    name="lock",
    description="lock a channel",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.MANAGE_CHANNELS,
    options=[interactions.Option(
                    name="channel",
                    description="channel to lock",
                    type=interactions.OptionType.CHANNEL,
                    required=False,
    )])
async def lock(ctx, channel=None):
    await ctx.get_guild()
    if channel == None:
        await ctx.get_channel()
        c = ctx.channel
        js = ctx.channel._json
    else:
        c = interactions.Channel(**await bot._http.get_channel(channel.id), _client=bot._http)
        js = c._json
    overwrites = [
        interactions.Overwrite(id = int(ctx.guild.id), type = 0, deny = interactions.Permissions.SEND_MESSAGES),
    ]
    await c.modify(permission_overwrites=overwrites)
    await ctx.send("Channel has been locked")
    

@bot.command(
    name="unlock",
    description="unlock a channel",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.MANAGE_CHANNELS,
    options=[interactions.Option(
                    name="channel",
                    description="channel to unlock",
                    type=interactions.OptionType.CHANNEL,
                    required=False,
    )])
async def unlock(ctx, channel=None):
    await ctx.get_guild()
    if channel == None:
        await ctx.get_channel()
        c = ctx.channel
        js = ctx.channel._json
    else:
        c = interactions.Channel(**await bot._http.get_channel(channel.id), _client=bot._http)
        js = c._json
    overwrites = [
        interactions.Overwrite(id = int(ctx.guild.id), type = 0, deny = None),
    ]
    await c.modify(permission_overwrites=overwrites)
    await ctx.send("Channel has been unlocked")
@bot.command(
    name="slowmode",
    description="slowmode a channel",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.MANAGE_CHANNELS,
    options=[interactions.Option(
                    name="channel",
                    description="channel to slowmode",
                    type=interactions.OptionType.CHANNEL,
                    required=True,
    ), interactions.Option(
                    name="seconds",
                    description="slowmode time in seconds max of 21600",
                    type=interactions.OptionType.INTEGER,
                    required=True,
    )])
async def slowmode(ctx, channel, seconds):
    await ctx.get_guild()
    if channel == None:
        await ctx.get_channel()
        c = ctx.channel
        js = ctx.channel._json
    else:
        c = interactions.Channel(**await bot._http.get_channel(channel.id), _client=bot._http)
        js = c._json
    if seconds > 21600:
        return await ctx.send("Limit of 21600")
    await c.modify(rate_limit_per_user=seconds)
    await ctx.send("Channel has been slowmoded")

def check_pinned(message):
    return not message.pinned

@bot.command(
    name="mpurge",
    description="purge a channel of messages",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.MANAGE_CHANNELS,
    options=[interactions.Option(
                    name="channel",
                    description="channel to purge",
                    type=interactions.OptionType.CHANNEL,
                    required=False,
    ),interactions.Option(
                    name="messages",
                    description="messages to purge",
                    type=interactions.OptionType.INTEGER,
                    required=False,
    )])
async def mpurge(ctx, channel=None, messages=None):
    await ctx.get_guild()
    if channel == None:
        await ctx.get_channel()
        c = ctx.channel
    else:
        c = interactions.Channel(**await bot._http.get_channel(channel.id), _client=bot._http)
    if messages == None:
        messages = 100
    l = await c.purge(messages, check=check_pinned)
    return await ctx.send(f"Purged {len(l)} messages")

@bot.command(
    name="warn",
    description="warn Someone",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.MODERATE_MEMBERS,
    options=[interactions.Option(
                    name="user",
                    description="user to warn",
                    type=interactions.OptionType.USER,
                    required=True,
    )])
async def warn(ctx,user):
    id = str(user.id)
    try:
        js[id]
    except:
        js[id] = 0
    n = js[id]
    await ctx.get_guild()
    if id == 977244263702224927:
        return await ctx.send("You cannot warn this bot")
    elif id == int(ctx.author.user.id):
        return await ctx.send("You cannot warn yourself")
    bb = await ctx.guild.get_member(int(bot.me.id))
    if user.roles == None:
        r = 0
    else:
        use = []
        for i in ctx.guild.roles:
            if int(i.id) in user.roles:
                use.append({"pos": i.position, "role": i})
        use.sort(key=funcc, reverse=True)
        r = use[0]["pos"]
    if ctx.author.roles == None:
        r2 = 0
    else:
        sel = []
        for i in ctx.guild.roles:
            if int(i.id) in ctx.author.roles:
                sel.append({"pos": i.position, "role": i})
        sel.sort(key=funcc, reverse=True)
        r2 = sel[0]["pos"]
    if bb.roles == 0:
        r3 = 0
    else:
        bo = []
        for i in ctx.guild.roles:
            if int(i.id) in bb.roles:
                bo.append({"pos": i.position, "role": i})
        bo.sort(key=funcc, reverse=True)
    #r = use[0]["pos"]
    #r2 = sel[0]["pos"]
    r3 = bo[0]["pos"]
    if r3<r:
        return await ctx.send("I do not have enough permissions to warn this person")
    if r2 > r:     
        if js[id] < 2:   
            js[id] += 1
        else:
            await user.kick(ctx.guild_id, reason="3 warnings")
            return await ctx.send("kicked for having 3 warnings")
    else:
        return await ctx.send("You cannot warn someone higher than yourself")
    await ctx.send(f"{user.user.username} has been warned")

@bot.command(
    name="warnlist",
    description="warn list",
    scope=918236915185115156,
    default_member_permissions=interactions.Permissions.MODERATE_MEMBERS,
    options=[interactions.Option(
                    name="user",
                    description="see warn list",
                    type=interactions.OptionType.USER,
                    required=True,
    )])
async def warnlist(ctx,user):
    id = str(user.id)
    try:
        js[id]
    except:
        js[id] = 0
    n = js[id]
    await ctx.send(f"{user.username} has {n} warns")
bot.start()