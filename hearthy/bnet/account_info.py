from enum import IntEnum
import logging
from hsproto import PegasusUtil_pb2, PegasusShared_pb2

class GameOption(IntEnum):
    AI_MODE = 0x30
    BACKGROUND_SOUND = 20
    BUNDLE_JUST_PURCHASE_IN_HUB = 0x6c
    CARD_BACK = 0x1c
    CARD_BACK2 = 0x1d
    CHANGED_CARDS_DATA = 0x24
    CONNECT_TO_AURORA = 0x1f
    COVER_MOUSE_OVERS = 0x2f
    CURSOR = 3
    DECK_PICKER_MODE = 0x36
    FAKE_PACK_COUNT = 14
    FAKE_PACK_OPENING = 13
    FRIENDS_LIST_CURRENTGAME_SECTION_HIDE = 0x3a
    FRIENDS_LIST_FRIEND_SECTION_HIDE = 0x3b
    FRIENDS_LIST_NEARBYPLAYER_SECTION_HIDE = 60
    FRIENDS_LIST_RECRUIT_SECTION_HIDE = 0x3d
    FRIENDS_LIST_REQUEST_SECTION_HIDE = 0x39
    GFX_FULLSCREEN = 10
    GFX_FXAA = 0x19
    GFX_HEIGHT = 9
    GFX_MSAA = 0x18
    GFX_QUALITY = 12
    GFX_TARGET_FRAME_RATE = 0x1a
    GFX_VSYNC = 0x1b
    GFX_WIDTH = 8
    GFX_WIN_CAMERA_CLEAR = 0x17
    GFX_WIN_POSX = 0x26
    GFX_WIN_POSY = 0x27
    HAS_ACKED_ARENA_REWARDS = 0x66
    HAS_ADDED_CARDS_TO_DECK = 0x58
    HAS_BEEN_NUDGED_TO_CM = 0x57
    HAS_CLICKED_TOURNAMENT = 0x3e
    HAS_CRAFTED = 0x5e
    HAS_DISENCHANTED = 0x5b
    HAS_ENTERED_NAXX = 0x6a
    HAS_FINISHED_A_DECK = 70
    HAS_LOST_IN_ARENA = 100
    HAS_OPENED_BOOSTER = 0x3f
    HAS_PLAYED_EXPERT_AI = 90
    HAS_PLAYED_NAXX = 0x6d
    HAS_RUN_OUT_OF_QUESTS = 0x65
    HAS_SEEN_100g_REMINDER = 0x61
    HAS_SEEN_ALL_BASIC_CLASS_CARDS_COMPLETE = 0x56
    HAS_SEEN_BRM = 0x73
    HAS_SEEN_CINEMATIC = 11
    HAS_SEEN_COLLECTIONMANAGER = 0x41
    HAS_SEEN_COLLECTIONMANAGER_AFTER_PRACTICE = 0x72
    HAS_SEEN_CRAFTING_INSTRUCTION = 0x5d
    HAS_SEEN_CUSTOM_DECK_PICKER = 0x55
    HAS_SEEN_DECK_HELPER = 0x52
    HAS_SEEN_EXPERT_AI = 80
    HAS_SEEN_EXPERT_AI_UNLOCK = 0x51
    HAS_SEEN_FORGE = 0x47
    HAS_SEEN_FORGE_1WIN = 0x4c
    HAS_SEEN_FORGE_2LOSS = 0x4d
    HAS_SEEN_FORGE_CARD_CHOICE = 0x49
    HAS_SEEN_FORGE_CARD_CHOICE2 = 0x4a
    HAS_SEEN_FORGE_HERO_CHOICE = 0x48
    HAS_SEEN_FORGE_PLAY_MODE = 0x4b
    HAS_SEEN_FORGE_RETIRE = 0x4e
    HAS_SEEN_GOLD_QTY_INSTRUCTION = 0x62
    HAS_SEEN_HEROIC_WARNING = 0x68
    HAS_SEEN_HUB = 0x45
    HAS_SEEN_LEVEL_3 = 0x63
    HAS_SEEN_MULLIGAN = 0x4f
    HAS_SEEN_NAXX = 0x69
    HAS_SEEN_NAXX_CLASS_CHALLENGE = 0x6b
    HAS_SEEN_PACK_OPENING = 0x53
    HAS_SEEN_PRACTICE_MODE = 0x54
    HAS_SEEN_PRACTICE_TRAY = 0x44
    HAS_SEEN_SHOW_ALL_CARDS_REMINDER = 0x5c
    HAS_SEEN_STEALTH_TAUNTER = 0x67
    HAS_SEEN_THE_COIN = 0x60
    HAS_SEEN_TOURNAMENT = 0x40
    HAS_STARTED_A_DECK = 0x71
    HEALTHY_GAMING_DEBUG = 15
    HUD = 4
    IDLE_KICK_TIME = 0x13
    IDLE_KICKER = 0x12
    IN_RANKED_PLAY_MODE = 0x5f
    INTRO = 0x2c
    INVALID = 0
    JUST_FINISHED_TUTORIAL = 0x42
    KELTHUZADTAUNTS = 0x25
    LAST_CUSTOM_DECK_CHOSEN = 0x35
    LAST_FAILED_DOP_VERSION = 0x29
    LAST_PRECON_HERO_CHOSEN = 0x34
    LAST_SCENE_MODE = 0x10
    LAST_SELECTED_STORE_ADVENTURE_ID = 0x70
    LAST_SELECTED_STORE_BOOSTER_ID = 0x6f
    LOCAL_TUTORIAL_PROGRESS = 30
    LOCALE = 0x11
    MUSIC = 2
    MUSIC_VOLUME = 7
    NEARBY_PLAYERS = 0x16
    PAGE_MOUSE_OVERS = 0x2e
    PREFERRED_CDN_INDEX = 40
    PREFERRED_REGION = 0x15
    RECONNECT = 0x21
    RECONNECT_RETRY_TIME = 0x23
    RECONNECT_TIMEOUT = 0x22
    SEASON_END_THRESHOLD = 0x20
    SELECTED_ADVENTURE = 0x37
    SELECTED_ADVENTURE_MODE = 0x38
    SHOW_ADVANCED_COLLECTIONMANAGER = 0x43
    SHOWN_GFX_DEVICE_WARNING = 0x2b
    SOUND = 1
    SOUND_VOLUME = 6
    SPECTATOR_OPEN_JOIN = 110
    STREAMING = 5
    TIP_CRAFTING_UNLOCKED = 0x59
    TIP_FORGE_PROGRESS = 0x33
    TIP_PLAY_PROGRESS = 50
    TIP_PRACTICE_PROGRESS = 0x31
    TOUCH_MODE = 0x2a
    TUTORIAL_LOST_PROGRESS = 0x2d

PRECON = PegasusUtil_pb2.DeckList()
for i in [7,31,274,637,671,813,893,930,1066]:
    PRECON.decks.add(id=i,
                     name="precon",
                     card_back=13,
                     hero=i,
                     deck_type=PegasusShared_pb2.DeckInfo.PRECON_DECK,
                     validity=31,
                     hero_premium=0,
                     card_back_override=False)

logger = logging.getLogger(__name__)

# Registration of GetAccountInfo handlers
_handlers = {}

def _handles(info_id):
    def regfun(fn):
        if info_id in _handlers:
            raise Exception('Double registration for info_id {}'.format(info_id))

        _handlers[info_id] = fn
        return fn

    return regfun

class AccountInfo:
    def __init__(self, account):
        self.account = account

    def handle(self, info_id):
        handler = _handlers.get(info_id, None)
        if handler is None:
            logger.warn('No handler found for info_id %d (%s)',
                        info_id,
                        PegasusUtil_pb2.GetAccountInfo.Request.Name(info_id))
            return None
        return _handlers[info_id](self)

    @_handles(PegasusUtil_pb2.GetAccountInfo.MEDAL_INFO)
    def get_medal_info(self):
        # TODO: currently not implemented
        return PegasusUtil_pb2.MedalInfo(
            season_wins=0,
            stars=20,
            streak=0,
            star_level=9,
            level_start=20,
            level_end=23,
            can_lose=True
        )

    @_handles(PegasusUtil_pb2.GetAccountInfo.DECK_LIST)
    def get_deck_list(self):
        deck_list = PegasusUtil_pb2.DeckList()
        deck_list.CopyFrom(PRECON)

        for deck in self.account.decks:
            deck_list.decks.add(id=deck.id,
                                name=deck.name,
                                card_back=13,
                                hero=deck.hero_id,
                                deck_type=PegasusShared_pb2.DeckInfo.NORMAL_DECK,
                                validity=31,
                                hero_premium=0,
                                card_back_override=False)

        return deck_list

    @_handles(PegasusUtil_pb2.GetAccountInfo.CARD_VALUES)
    def get_card_values(self):
        # TODO: figure out what card_nerf_index is used for
        cv = PegasusUtil_pb2.CardValues(card_nerf_index=5)
        for item in self.account.crafting_cost['list']:
            entry = cv.cards.add(buy=item['buy'],sell=item['sell'],nerfed=False)
            entry.card.asset = item['card_id']
            if item.get('premium', 0) > 0:
                entry.card.premium = item['premium']
        return cv

    @_handles(PegasusUtil_pb2.GetAccountInfo.BOOSTERS)
    def get_boosters(self):
        return PegasusUtil_pb2.BoosterList()

    @_handles(PegasusUtil_pb2.GetAccountInfo.FEATURES)
    def get_features(self):
        return PegasusUtil_pb2.GuardianVars(showUserUI=1)

    @_handles(PegasusUtil_pb2.GetAccountInfo.CAMPAIGN_INFO)
    def get_campaign_info(self):
        return PegasusUtil_pb2.ProfileProgress(
            progress=6,
            best_forge=10,
            last_forge=PegasusShared_pb2.Date(
                year=2015,
                month=3,
                day=31,
                hours=17,
                min=3,
                sec=54
            )
        )

    @_handles(PegasusUtil_pb2.GetAccountInfo.CARD_BACKS)
    def get_card_backs(self):
        return PegasusUtil_pb2.CardBacks(
            default_card_back=13,
            card_backs=list(range(1,20)))

    @_handles(PegasusUtil_pb2.GetAccountInfo.GOLD_BALANCE)
    def get_gold_balance(self):
        """ Returns the current gold balance. """
        balance = self.account.balances['gold']

        return PegasusUtil_pb2.GoldBalance(
            capped_balance=balance,
            bonus_balance=0,
            cap=999999,
            cap_warning=999999)

    @_handles(PegasusUtil_pb2.GetAccountInfo.ARCANE_DUST_BALANCE)
    def get_arcane_dust_balance(self):
        """ Returns the current arcane dust balance. """
        balance = self.account.balances['arcane_dust']
        return PegasusUtil_pb2.ArcaneDustBalance(balance=balance)

    @_handles(PegasusUtil_pb2.GetAccountInfo.NOTICES)
    def get_notices(self):
        # TODO: currently not implemented
        return PegasusUtil_pb2.ProfileNotices()

    @_handles(PegasusUtil_pb2.GetAccountInfo.REWARD_PROGRESS)
    def get_reward_progress(self):
        # TODO: currently not implemented
        return PegasusUtil_pb2.RewardProgress(
            season_end=PegasusShared_pb2.Date(
                year=2015,
                month=4,
                day=30,
                hours=22,
                min=0,
                sec=0
            ),
            wins_per_gold=3,
            gold_per_reward=10,
            max_gold_per_day=100,
            season_number=18,
            xp_solo_limit=60,
            max_hero_level=60,
            next_quest_cancel=PegasusShared_pb2.Date(
                year=2015,
                month=4,
                day=1,
                hours=0,
                min=0,
                sec=0
            ),
            event_timing_mod=-0.0833333283662796
        )

    @_handles(PegasusUtil_pb2.GetAccountInfo.PLAYER_RECORD)
    def get_player_records(self):
        # TODO: currently not implemented
        return PegasusUtil_pb2.PlayerRecords()

    @_handles(PegasusUtil_pb2.GetAccountInfo.CLIENT_OPTIONS)
    def get_client_options(self):
        opts = PegasusUtil_pb2.ClientOptions()

        for name, value in self.account.options:
            opt = opts.options.add(index=GameOption[name])
            setattr(opt, value['type'], value['payload'])

        return opts

    @_handles(PegasusUtil_pb2.GetAccountInfo.COLLECTION)
    def get_collection(self):
        coll = PegasusUtil_pb2.Collection()
        for card_item in self.account.collection.cards['list']:
            entry = coll.stacks.add()
            entry.count = card_item['count']
            entry.num_seen = entry.count

            entry.card_def.asset = card_item['card_id']
            if card_item.get('premium', 0) > 0:
                entry.card_def.premium = card_item['premium']

            entry.latest_insert_date.year = 2010
            entry.latest_insert_date.month = 1
            entry.latest_insert_date.day = 1
            entry.latest_insert_date.hours = 0
            entry.latest_insert_date.min = 0
            entry.latest_insert_date.sec = 0

        return coll

    @_handles(PegasusUtil_pb2.GetAccountInfo.HERO_XP)
    def get_hero_xp(self):
        # TODO: not implemented
        xp = PegasusUtil_pb2.HeroXP()

        for i in range(2,11):
            xp.xp_infos.add(class_id=i,level=60,curr_xp=1480,max_xp=1480)

        return xp

    @_handles(PegasusUtil_pb2.GetAccountInfo.BOOSTER_TALLY)
    def get_booster_tally(self):
        # TODO: not implemented
        return PegasusUtil_pb2.BoosterTallyList()

    @_handles(PegasusUtil_pb2.GetAccountInfo.DECK_LIMIT)
    def get_profile_deck_limit(self):
        # TODO: not implemented
        return PegasusUtil_pb2.ProfileDeckLimit(deck_limit=9)

    @_handles(PegasusUtil_pb2.GetAccountInfo.MASSIVE_LOGIN)
    def get_massive_login(self):
        return PegasusUtil_pb2.MassiveLoginReply(
            profile_progress=self.get_campaign_info(),
            medal_info=self.get_medal_info(),
            deck_list=self.get_deck_list(),
            gold_balance=self.get_gold_balance(),
            arcane_dust_balance=self.get_arcane_dust_balance(),
            profile_deck_limit=self.get_profile_deck_limit(),
            reward_progress=self.get_reward_progress(),
            player_records=self.get_player_records(),
            card_backs=self.get_card_backs()
        )
