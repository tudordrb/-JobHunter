from app.models import Job


# =========================================================
# HARD REJECTION KEYWORDS
# Orice job care conține aceste expresii este respins direct.
# =========================================================

REJECT_KEYWORDS = [

    # -----------------------------------------------------
    # FILMARE / PREZENȚĂ FIZICĂ / UGC
    # -----------------------------------------------------

    "filming required",
    "must film",
    "must shoot",
    "shoot footage",
    "shoot content",
    "record yourself",
    "record videos",
    "create footage",
    "capture footage",
    "videographer",
    "cinematographer",
    "camera operator",
    "camera person",
    "camera crew",
    "production crew",
    "on-site",
    "onsite",
    "in person",
    "in-person",
    "local only",
    "must be located",
    "must live in",
    "must be based in",
    "travel required",
    "location shoot",
    "studio shoot",
    "product shoot",
    "photo shoot",
    "photoshoot",
    "shooting day",
    "shoot day",
    "ugc creator",
    "ugc creators",
    "ugc content creator",
    "ugc model",
    "selfies needed",
    "selfie needed",
    "face required",
    "appear on camera",
    "be on camera",
    "talking to camera",
    "record voice",
    "voice recording",
    "voice-over required",
    "voiceover required",
    "actor required",
    "actress required",
    "model required",
    "content creator needed",
    "create original footage",

    # -----------------------------------------------------
    # SOCIAL MEDIA MANAGEMENT / POSTING / STRATEGY
    # -----------------------------------------------------

    "social media manager",
    "social media management",
    "community manager",
    "community management",
    "content manager",
    "content management",
    "manage instagram",
    "manage tiktok",
    "manage facebook",
    "manage social media",
    "posting schedule",
    "content calendar",
    "content strategy",
    "social media strategy",
    "schedule posts",
    "publish posts",
    "upload posts",
    "posting required",
    "engagement management",
    "reply to comments",
    "reply to messages",
    "grow followers",
    "account growth",
    "organic growth",
    "social growth",
    "hashtag strategy",
    "analytics reporting",
    "social analytics",

    # -----------------------------------------------------
    # ADS MANAGEMENT / MARKETING MANAGEMENT
    # -----------------------------------------------------

    "facebook ads manager",
    "meta ads manager",
    "google ads",
    "ads management",
    "ad campaign management",
    "campaign management",
    "media buyer",
    "media buying",
    "performance marketer",
    "digital marketer",
    "marketing manager",
    "lead generation",
    "seo",
    "email marketing",
    "marketing strategy",

    # -----------------------------------------------------
    # COPYWRITING / WRITING
    # -----------------------------------------------------

    "copywriter",
    "copywriting",
    "content writing",
    "article writing",
    "blog writing",
    "script writer",
    "scriptwriter",
    "write scripts",
    "caption writing",
    "write captions",
    "seo writing",
    "proofreading",
    "translation",

    # -----------------------------------------------------
    # GRAPHIC DESIGN / BRANDING / LOGO
    # -----------------------------------------------------

    "logo design",
    "logo designer",
    "logo redesign",
    "logo conversion",
    "brand identity",
    "brand guidelines",
    "brand book",
    "visual identity",
    "graphic designer",
    "graphic design",
    "brochure design",
    "flyer design",
    "poster design",
    "business card design",
    "packaging design",
    "t-shirt design",
    "t shirt design",
    "merch design",
    "fashion design",
    "illustration",
    "illustrator",
    "digital illustration",
    "vector illustration",
    "vector tracing",
    "vectorization",
    "coreldraw",
    "cdr",
    "adobe illustrator",
    "canva design",
    "presentation design",
    "powerpoint design",
    "ui design",
    "ux design",
    "web design",
    "website design",
    "landing page design",
    "figma",
    "3d design",
    "3d modeling",
    "3d modelling",
    "cad",
    "autocad",

    # -----------------------------------------------------
    # ANIMAȚIE / 3D GREU / VFX SPECIALIZAT
    # -----------------------------------------------------

    "3d animation",
    "character animation",
    "rigging",
    "blender",
    "maya",
    "cinema 4d",
    "c4d",
    "unreal engine",
    "unity",
    "vfx artist",
    "visual effects artist",
    "compositing artist",
    "rotoscoping",
    "cgi",
    "3d render",
    "3d rendering",

    # -----------------------------------------------------
    # AUDIO-ONLY
    # -----------------------------------------------------

    "audio editor",
    "audio editing only",
    "podcast audio editor",
    "music producer",
    "sound engineer",
    "audio engineer",
    "mixing engineer",
    "mastering engineer",
    "noise removal only",

    # -----------------------------------------------------
    # DEVELOPMENT / TECH
    # -----------------------------------------------------

    "web developer",
    "developer",
    "software developer",
    "app developer",
    "wordpress",
    "shopify developer",
    "coding",
    "programming",
    "python developer",
    "javascript",
    "react",
    "html",
    "css",

    # -----------------------------------------------------
    # ECOMMERCE / VA / ADMIN
    # -----------------------------------------------------

    "virtual assistant",
    "data entry",
    "customer support",
    "customer service",
    "product listing",
    "amazon listing",
    "ebay listing",
    "shopify manager",
    "store manager",

    # -----------------------------------------------------
    # STRICT / MICROMANAGEMENT
    # -----------------------------------------------------

    "strict template",
    "follow exact template",
    "follow this exact template",
    "frame-by-frame",
    "frame by frame",
    "replicate exactly",
    "copy exactly",
    "must match exactly",
    "pixel perfect",
    "no creative freedom",
    "no creative input",
    "do not change anything",
    "exact instructions",
    "strict instructions",
    "multiple daily revisions",
    "unlimited revisions",
]


# =========================================================
# VIDEO EDITING POSITIVE KEYWORDS
# Cel puțin unul trebuie să existe pentru joburile video.
# =========================================================

VIDEO_POSITIVE_KEYWORDS = [
    "video editing",
    "video editor",
    "video post-editing",
    "video post editing",
    "video post-production",
    "video post production",
    "short-form video",
    "short form video",
    "short-form editor",
    "short form editor",
    "reels editor",
    "instagram reels",
    "reels",
    "tiktok editor",
    "tiktok video editor",
    "tiktok",
    "youtube shorts",
    "shorts editor",
    "social media video editor",
    "ad video editor",
    "video ads",
    "video ad editing",
    "facebook video editor",
    "meta video editor",
    "instagram video editor",
    "product video editing",
    "podcast clips",
    "podcast video editing",
    "talking head editing",
    "talking-head editing",
    "captions",
    "subtitles",
    "color grading",
    "colour grading",
    "sound design",
    "premiere pro",
    "adobe premiere pro",
    "after effects",
    "capcut",
    "davinci resolve",
    "final cut pro",
    "motion graphics",
]


# =========================================================
# PHOTO EDITING POSITIVE KEYWORDS
# =========================================================

PHOTO_POSITIVE_KEYWORDS = [
    "photo editing",
    "photo editor",
    "image editing",
    "image editor",
    "photo retouching",
    "photo retoucher",
    "retouching",
    "image retouching",
    "photoshop editing",
    "photoshop retouching",
    "lightroom editing",
    "adobe lightroom",
    "adobe photoshop",
    "color correction",
    "colour correction",
    "photo color correction",
    "photo colour correction",
    "skin retouching",
    "portrait retouching",
    "product photo editing",
    "real estate photo editing",
    "background removal",
    "remove background",
    "image cleanup",
    "photo manipulation",
    "image enhancement",
    "photo enhancement",
    "photo restoration",
]


# =========================================================
# TERMENI CARE SUGEREAZĂ CĂ ESTE STRICT EDITARE
# =========================================================

EDITING_CONTEXT_KEYWORDS = [
    "raw footage provided",
    "footage provided",
    "client provides footage",
    "we provide footage",
    "assets provided",
    "raw files provided",
    "source files provided",
    "photos provided",
    "images provided",
    "edit provided footage",
    "edit existing footage",
    "edit existing photos",
    "post-production",
    "post production",
    "turn raw footage into",
    "transform raw footage",
    "edit clips",
    "edit videos",
    "edit photos",
]


def should_reject(job: Job):
    """
    Returnează:
    (True, motiv)  -> job respins
    (False, motiv) -> job acceptat de hard filters

    IMPORTANT:
    Funcția asta NU decide dacă jobul este excelent.
    Decide doar dacă merită să ajungă mai departe la AI/scoring.
    """

    text = f"{job.title} {job.description}".lower()

    # =====================================================
    # 1. REMOTE ONLY
    # =====================================================

    if not job.remote:
        return True, "Jobul nu este remote"

    # =====================================================
    # 2. HARD REJECTION
    # =====================================================

    for keyword in REJECT_KEYWORDS:
        if keyword in text:
            return True, f"Respins: '{keyword}'"

    # =====================================================
    # 3. DETECTĂM CE TIP DE EDITARE ESTE
    # =====================================================

    video_match = any(
        keyword in text
        for keyword in VIDEO_POSITIVE_KEYWORDS
    )

    photo_match = any(
        keyword in text
        for keyword in PHOTO_POSITIVE_KEYWORDS
    )

    # Dacă nu este nici editare video, nici foto, pleacă.
    if not video_match and not photo_match:
        return True, "Nu este relevant pentru editare foto/video"

    # =====================================================
    # 4. FILTRU SUPLIMENTAR PENTRU JOBURI AMBIGUE
    # =====================================================

    editing_context = any(
        keyword in text
        for keyword in EDITING_CONTEXT_KEYWORDS
    )

    # Dacă jobul pare video/foto, dar cere și lucruri dubioase,
    # îl lăsăm pentru moment dacă are termeni clari de editing.
    # AI-ul îl va analiza mai târziu.
    if editing_context:
        if video_match and photo_match:
            return False, "Editare foto + video relevantă"

        if video_match:
            return False, "Editare video relevantă"

        if photo_match:
            return False, "Editare foto relevantă"

    # =====================================================
    # 5. ACCEPTARE PE BAZA SKILL-ULUI PRINCIPAL
    # =====================================================

    if video_match and not photo_match:
        return False, "Editare video relevantă"

    if photo_match and not video_match:
        return False, "Editare foto relevantă"

    if video_match and photo_match:
        return False, "Editare foto/video relevantă"

    return True, "Respins de filtrul final"