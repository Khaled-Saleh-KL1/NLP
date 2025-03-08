arabic_patterns = [
    (r"\b(مرحبا|السلام عليكم|أهلا)\b.*", "مرحبًا! كيف يمكنني مساعدتك اليوم؟"),
    (r".*\b(من أنت)\b.*", "أنا مساعد افتراضي هنا لمساعدتك. كيف يمكنني خدمتك؟"),
    (r".*\b(ما اسمك)\b.*", "أنا مساعدك الشخصي! كيف يمكنني مساعدتك؟"),
    (r".*\b(كيف حالك)\b.*", "أنا مجرد برنامج، لكنني هنا دائمًا لمساعدتك!"),
    
    (r"\b(?:أنا|انا) (\w+)$", r"آسف أن أسمع أنك \1، هل يمكنك مشاركة المزيد؟"),
    (r"\b(?:أنا|انا) (\w+) (\w+)$", r"لماذا تشعر أنك \1 \2؟"),
    (r"\b(?:أنا|انا) (\w+) (\w+) (\w+)$", r"هل هناك أسباب محددة تجعلك تشعر بال\1 \2 \3؟"),
    (r"\b(?:أنا|انا) (\w+) (\w+) (\w+) (\w+)$", r"هل يمكنك شرح أكثر عن شعورك بال\1 \2 \3 \4؟"),
    
    (r".*\b(دائمًا|كل الوقت|كثيرًا)\b.*", "هل يمكنك ذكر مثال محدد؟"),
    (r".*\b(لا أستطيع)\b.*", "لماذا تجد صعوبة في \1؟"),
    (r".*\b(أريد) (\w+)\b.*", "لماذا ترغب في \2 بالذات؟"),
    
    (r"\b(هل)\b.*", "لماذا تتساءل عن \1؟"),
    (r"\b(لماذا)\b.*", "ما الذي يدفعك لسؤال \1؟"),
    (r"\b(كيف)\b.*", "كيف تعتقد أن \1 يمكن أن يساعدك؟"),
    
    (r".*\b(حزين|مكتئب|قلق|خائف|مرهق|محبط|غاضب|مذنب)\b.*", r"لماذا تشعر بال\1؟"),
    (r".*\b(أفكر في)\b.*", "هل يمكنك مشاركة ما تفكر فيه؟"),
    (r".*\b(لا أعرف)\b.*", "هل هناك شيء محدد لا تستطيع تحديده؟"),
    
    (r".*\b(مشكلة|صعوبة|مشكلات|عقبات|تحديات)\b.*", "هل يمكنك شرح المشكلة أكثر؟"),
    (r".*\b(أحتاج)\b.*", "لماذا تشعر أنك تحتاج إلى \1؟"),
    (r".*\b(لا أستطيع) (\w+)\b.*", "لماذا تجد صعوبة في \2؟"),
    (r".*\b(أريد) (\w+)\b.*", "لماذا ترغب في \2؟"),
    
    (r".*\b(لا)\b.*", "هل هناك شيء إيجابي يمكنك مشاركته؟"),
    (r".*\b(لا أحد)\b.*", "هل حاولت التحدث إلى شخص ما؟"),
    
    (r".*\b(الانتحار|القتل|الموت|إيذاء النفس|الانهيار)\b.*", "هذه حالة خطيرة. هل يمكنك الاتصال بمساعد طبي أو خط أمان؟"),

    (r".*\b(أشعر بالضياع|أشعر بالوحدة|أشعر بالعجز)\b.*", r"أنا هنا لأستمع إليك. ما الذي يجعلك تشعر بال\1؟"),
    (r".*\b(لا أستطيع النوم|أعاني من الأرق)\b.*", r"الأرق قد يكون مرتبطًا بالتوتر. هل هناك شيء يقلقك؟"),
    (r".*\b(أريد التحدث|أحتاج إلى شخص أتحدث معه)\b.*", r"أنا هنا لأسمعك. ما الذي يزعجك؟"),
    (r".*\b(أشعر أن لا أحد يفهمني)\b.*", r"أنا هنا لأفهمك. هل يمكنك مشاركة ما تشعر به؟"),
    (r".*\b(أشعر باليأس|لا أرى مخرجًا)\b.*", r"أنا هنا لدعمك. لنبحث معًا عن حلول."),
    (r".*\b(أشعر أنني فاشل)\b.*", r"كلنا نواجه صعوبات. هذا لا يعني أنك فاشل."),
    (r".*\b(لا أستطيع التحمل)\b.*", r"أنت أقوى مما تعتقد. دعنا نبحث عن طرق لتخفيف العبء."),
    (r".*\b(ماذا أفعل؟|لا أعرف كيف أتعامل)\b.*", r"لنبدأ بخطوات صغيرة. ما الذي يمكنك فعله الآن لتحسين حالتك؟"),
    (r".*\b(أشعر بالتوتر الشديد)\b.*", r"التنفس العميق أو التأمل قد يساعد. هل جربت ذلك؟"),
    (r".*\b(لا أستطيع التركيز)\b.*", r"حاول تقسيم المهام إلى أجزاء صغيرة. هذا قد يسهل الأمور."),
    (r".*\b(أفكر في الانتحار|أريد إنهاء حياتي)\b.*", r"هذا أمر خطير. الرجاء الاتصال بخط مساعدة أو طبيب نفسي فورًا."),
    (r".*\b(لا أستطيع التعامل مع حياتي)\b.*", r"قد يكون التحدث إلى مختص مفيدًا. هل فكرت في طلب مساعدة مهنية؟"),
    (r".*\b(أشعر أنني بحاجة إلى مساعدة)\b.*", r"طلب المساعدة خطوة شجاعة. هل يمكنني مساعدتك في العثور على موارد؟"),
]

english_patterns = [
    (r"\b(hello|hi|hey)\b.*", "Hello! How can I assist you today?"),
    (r".*\b(who are you)\b.*", "I am a virtual assistant here to help you. How can I serve you?"),
    (r".*\b(what is your name)\b.*", "I am your personal assistant! How can I help you?"),
    (r".*\b(how are you)\b.*", "I'm just a program, but I'm always here to help you!"),
    
    (r"\b(I am|I'm) (\w+)$", r"I'm sorry to hear that you're \2. Can you share more?"),
    (r"\b(I am|I'm) (\w+) (\w+)$", r"Why do you feel \1 \2?"),
    (r"\b(I am|I'm) (\w+) (\w+) (\w+)$", r"Are there specific reasons why you feel \1 \2 \3?"),
    (r"\b(I am|I'm) (\w+) (\w+) (\w+) (\w+)$", r"Can you explain more about feeling \1 \2 \3 \4?"),
    
    (r".*\b(always|all the time|often)\b.*", "Can you give a specific example?"),
    (r".*\b(I can't)\b.*", "Why do you find it difficult to \1?"),
    (r".*\b(I want) (\w+)\b.*", "Why do you want \2 specifically?"),
    
    (r"\b(is)\b.*", "Why are you wondering about \1?"),
    (r"\b(why)\b.*", "What makes you ask \1?"),
    (r"\b(how)\b.*", "How do you think \1 can help you?"),
    
    (r".*\b(sad|depressed|anxious|scared|exhausted|frustrated|angry|guilty)\b.*", r"Why do you feel \1?"),
    (r".*\b(I think about)\b.*", "Can you share what you're thinking about?"),
    (r".*\b(I don't know)\b.*", "Is there something specific you can't identify?"),
    
    (r".*\b(problem|difficulty|problems|obstacles|challenges)\b.*", "Can you explain the problem further?"),
    (r".*\b(I need)\b.*", "Why do you feel you need \1?"),
    (r".*\b(I can't) (\w+)\b.*", "Why do you find it difficult to \2?"),
    (r".*\b(I want) (\w+)\b.*", "Why do you want \2?"),
    
    (r".*\b(no)\b.*", "Is there something positive you can share?"),
    (r".*\b(no one)\b.*", "Have you tried talking to someone?"),
    
    (r".*\b(suicide|killing|death|self-harm|breakdown)\b.*", "This is serious. Can you contact a medical professional or helpline?"),

    (r".*\b(I feel lost|I feel lonely|I feel helpless)\b.*", r"I'm here to listen. What's making you feel \1?"),
    (r".*\b(I can't sleep|I have insomnia)\b.*", r"Insomnia can be linked to stress. Is something worrying you?"),
    (r".*\b(I want to talk|I need someone to talk to)\b.*", r"I'm here to listen. What's bothering you?"),
    (r".*\b(I feel like no one understands me)\b.*", r"I'm here to understand you. Can you share what you're feeling?"),
    (r".*\b(I feel hopeless|I don't see a way out)\b.*", r"I'm here to support you. Let's look for solutions together."),
    (r".*\b(I feel like a failure)\b.*", r"We all face challenges. That doesn't mean you're a failure."),
    (r".*\b(I can't handle it)\b.*", r"You're stronger than you think. Let's find ways to ease the burden."),
    (r".*\b(What should I do?|I don't know how to cope)\b.*", r"Let's start with small steps. What can you do right now to feel better?"),
    (r".*\b(I feel extremely stressed)\b.*", r"Deep breathing or meditation might help. Have you tried that?"),
    (r".*\b(I can't focus)\b.*", r"Try breaking tasks into smaller parts. That might make things easier."),
    (r".*\b(I'm thinking about suicide|I want to end my life)\b.*", r"This is serious. Please contact a helpline or mental health professional immediately."),
    (r".*\b(I can't handle my life)\b.*", r"Talking to a professional might help. Have you considered seeking help?"),
    (r".*\b(I feel like I need help)\b.*", r"Seeking help is a brave step. Can I help you find resources?"),
]