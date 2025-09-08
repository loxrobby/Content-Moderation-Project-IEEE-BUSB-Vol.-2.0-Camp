#!/usr/bin/env python3
"""
Comprehensive Spam Keywords Generator
====================================

This script generates an extensive list of spam keywords covering:
- Financial spam (loans, investments, crypto)
- Health/medical spam (pharmaceuticals, supplements)
- Dating/relationship spam
- Gambling/casino spam
- Business/MLM spam
- Technology spam
- Travel/vacation spam
- Education/course spam
- Real estate spam
- Automotive spam
- And many more categories
"""

def generate_comprehensive_spam_keywords():
    """
    Generate a comprehensive list of spam keywords organized by category.
    """
    
    spam_keywords = {
        # Financial and Investment Spam
        'financial': [
            # Loans and Credit
            'loan', 'loans', 'lending', 'lender', 'borrow', 'borrowing', 'credit', 'credits', 'debt', 'debt consolidation',
            'refinance', 'refinancing', 'mortgage', 'mortgages', 'home loan', 'personal loan', 'business loan',
            'payday loan', 'cash advance', 'quick loan', 'instant loan', 'no credit check', 'bad credit',
            'poor credit', 'credit repair', 'credit score', 'credit report', 'credit monitoring',
            
            # Money and Cash
            'money', 'cash', 'dollars', 'currency', 'funds', 'financing', 'capital', 'investment', 'invest',
            'investing', 'investor', 'investors', 'portfolio', 'wealth', 'rich', 'richer', 'richest',
            'millionaire', 'billionaire', 'affluent', 'prosperous', 'financial freedom', 'financial independence',
            'passive income', 'residual income', 'recurring income', 'monthly income', 'weekly income',
            'daily income', 'earn money', 'make money', 'get rich', 'become rich', 'quick cash',
            'fast cash', 'easy money', 'guaranteed income', 'risk-free', 'no risk', 'low risk',
            
            # Investment Scams
            'forex', 'forex trading', 'currency trading', 'binary options', 'cryptocurrency', 'crypto',
            'bitcoin', 'btc', 'ethereum', 'eth', 'altcoin', 'altcoins', 'trading', 'trader', 'traders',
            'day trading', 'swing trading', 'scalping', 'pips', 'leverage', 'margin', 'broker', 'brokers',
            'trading platform', 'trading software', 'trading signals', 'trading alerts', 'trading bot',
            'automated trading', 'robot trading', 'ai trading', 'machine learning trading',
            
            # MLM and Pyramid Schemes
            'network marketing', 'mlm', 'multi-level marketing', 'direct sales', 'pyramid scheme',
            'get rich quick', 'work from home', 'home business', 'online business', 'internet business',
            'business opportunity', 'business opportunities', 'start your own business', 'be your own boss',
            'financial freedom', 'time freedom', 'location freedom', 'residual income', 'passive income',
            'recruit', 'recruiting', 'recruitment', 'team building', 'downline', 'upline', 'sponsor',
            'mentor', 'coach', 'leader', 'leadership', 'success', 'successful', 'achievement',
        ],
        
        # Health and Medical Spam
        'health_medical': [
            # Pharmaceuticals
            'viagra', 'cialis', 'levitra', 'pharmacy', 'pharmacies', 'medication', 'medications',
            'prescription', 'prescriptions', 'drug', 'drugs', 'pill', 'pills', 'tablet', 'tablets',
            'capsule', 'capsules', 'supplement', 'supplements', 'vitamin', 'vitamins', 'herbal',
            'natural', 'organic', 'homeopathic', 'alternative medicine', 'holistic', 'wellness',
            
            # Weight Loss and Fitness
            'weight loss', 'lose weight', 'fat loss', 'burn fat', 'slim', 'slimming', 'diet', 'diets',
            'dieting', 'diet pill', 'diet pills', 'fat burner', 'fat burners', 'metabolism', 'metabolic',
            'fitness', 'exercise', 'workout', 'muscle', 'muscles', 'protein', 'protein powder',
            'testosterone', 'hormone', 'hormones', 'steroid', 'steroids', 'bodybuilding', 'gym',
            'fitness program', 'fitness plan', 'fitness routine', 'personal trainer', 'coach',
            
            # Medical Conditions
            'diabetes', 'diabetic', 'blood sugar', 'cholesterol', 'high blood pressure', 'hypertension',
            'heart disease', 'cancer', 'tumor', 'tumors', 'cure', 'cures', 'treatment', 'treatments',
            'therapy', 'therapies', 'healing', 'heal', 'recovery', 'recover', 'rehabilitation',
            'chronic pain', 'arthritis', 'inflammation', 'immune system', 'immunity', 'allergy',
            'allergies', 'asthma', 'depression', 'anxiety', 'stress', 'insomnia', 'sleep',
        ],
        
        # Dating and Relationship Spam
        'dating_relationship': [
            'dating', 'date', 'dates', 'single', 'singles', 'marriage', 'marry', 'married', 'divorce',
            'relationship', 'relationships', 'love', 'lover', 'lovers', 'romance', 'romantic',
            'partner', 'partners', 'companion', 'companions', 'match', 'matches', 'matching',
            'compatibility', 'soulmate', 'soulmates', 'true love', 'perfect match', 'ideal partner',
            'adult dating', 'mature dating', 'senior dating', 'local dating', 'online dating',
            'speed dating', 'blind date', 'first date', 'hookup', 'hookups', 'casual dating',
            'serious relationship', 'long term relationship', 'commitment', 'engagement', 'wedding',
            'bride', 'groom', 'bridesmaid', 'groomsman', 'honeymoon', 'anniversary',
            
            # Adult Content
            'adult', 'adults', 'porn', 'pornography', 'pornographic', 'xxx', 'sex', 'sexual',
            'sexy', 'sexy', 'erotic', 'erotica', 'nude', 'naked', 'nudity', 'nudist', 'nudists',
            'escort', 'escorts', 'massage', 'massages', 'therapeutic massage', 'sensual massage',
            'tantric', 'tantra', 'fetish', 'fetishes', 'bdsm', 'domination', 'submission',
            'swinger', 'swingers', 'swinging', 'threesome', 'orgy', 'orgies', 'fetish dating',
        ],
        
        # Gambling and Casino Spam
        'gambling_casino': [
            'casino', 'casinos', 'gambling', 'gamble', 'gambler', 'gamblers', 'bet', 'bets', 'betting',
            'poker', 'poker room', 'poker tournament', 'texas holdem', 'blackjack', 'black jack',
            'roulette', 'slot', 'slots', 'slot machine', 'slot machines', 'lottery', 'lotto',
            'jackpot', 'jackpots', 'win', 'winner', 'winners', 'winning', 'winnings', 'prize',
            'prizes', 'bonus', 'bonuses', 'reward', 'rewards', 'lucky', 'luck', 'chance', 'chances',
            'odds', 'probability', 'house edge', 'rake', 'rake back', 'comp', 'comps', 'vip',
            'high roller', 'whale', 'whales', 'sportsbook', 'sports betting', 'live betting',
            'in-play betting', 'odds', 'spread', 'over under', 'parlay', 'teaser', 'futures',
            'prop bet', 'prop bets', 'live casino', 'live dealer', 'live games', 'virtual casino',
            'online casino', 'mobile casino', 'casino app', 'casino bonus', 'welcome bonus',
            'no deposit bonus', 'free spins', 'free play', 'demo play', 'practice mode',
        ],
        
        # Technology and Software Spam
        'technology_software': [
            # Software and Apps
            'software', 'app', 'apps', 'application', 'applications', 'program', 'programs',
            'download', 'downloads', 'downloading', 'install', 'installation', 'installing',
            'update', 'updates', 'updating', 'upgrade', 'upgrades', 'upgrading', 'patch', 'patches',
            'version', 'versions', 'latest version', 'new version', 'beta', 'beta version',
            'trial', 'trials', 'free trial', 'demo', 'demos', 'demo version', 'full version',
            'premium', 'premium version', 'pro version', 'professional', 'enterprise',
            
            # Security and Antivirus
            'antivirus', 'anti-virus', 'virus', 'viruses', 'malware', 'spyware', 'adware',
            'trojan', 'trojans', 'worm', 'worms', 'rootkit', 'rootkits', 'backdoor', 'backdoors',
            'firewall', 'firewalls', 'security', 'secure', 'protection', 'protect', 'protecting',
            'scan', 'scans', 'scanning', 'clean', 'cleaning', 'remove', 'removing', 'delete',
            'deleting', 'quarantine', 'quarantining', 'threat', 'threats', 'vulnerability',
            'vulnerabilities', 'exploit', 'exploits', 'hack', 'hacker', 'hackers', 'hacking',
            'breach', 'breaches', 'data breach', 'security breach', 'password', 'passwords',
            'login', 'logins', 'account', 'accounts', 'profile', 'profiles', 'identity theft',
            
            # Internet and Web
            'internet', 'web', 'website', 'websites', 'domain', 'domains', 'hosting', 'host',
            'server', 'servers', 'cloud', 'cloud computing', 'storage', 'backup', 'backups',
            'email', 'emails', 'spam', 'spamming', 'phishing', 'scam', 'scams', 'scamming',
            'fraud', 'fraudulent', 'fake', 'counterfeit', 'illegal', 'unauthorized', 'pirated',
        ],
        
        # Business and MLM Spam
        'business_mlm': [
            'business', 'businesses', 'company', 'companies', 'corporation', 'corporations',
            'enterprise', 'enterprises', 'startup', 'startups', 'entrepreneur', 'entrepreneurs',
            'entrepreneurship', 'business plan', 'business model', 'revenue', 'revenues',
            'profit', 'profits', 'profitable', 'profitability', 'income', 'earnings', 'sales',
            'marketing', 'advertising', 'promotion', 'promotions', 'promotional', 'campaign',
            'campaigns', 'strategy', 'strategies', 'tactics', 'techniques', 'methods', 'systems',
            'process', 'processes', 'workflow', 'workflows', 'automation', 'automated',
            'efficiency', 'efficient', 'productivity', 'productive', 'optimization', 'optimize',
            'scalability', 'scalable', 'growth', 'expansion', 'development', 'developing',
            'innovation', 'innovative', 'disruption', 'disruptive', 'transformation',
            'digital transformation', 'digital marketing', 'online marketing', 'social media',
            'seo', 'search engine optimization', 'ppc', 'pay per click', 'cpc', 'cost per click',
            'cpm', 'cost per mille', 'roi', 'return on investment', 'conversion', 'conversions',
            'lead', 'leads', 'lead generation', 'prospect', 'prospects', 'prospecting',
            'customer', 'customers', 'client', 'clients', 'audience', 'target audience',
        ],
        
        # Travel and Vacation Spam
        'travel_vacation': [
            'travel', 'traveling', 'travelling', 'trip', 'trips', 'vacation', 'vacations',
            'holiday', 'holidays', 'getaway', 'getaways', 'escape', 'escapes', 'adventure',
            'adventures', 'journey', 'journeys', 'tour', 'tours', 'tourism', 'tourist',
            'tourists', 'destination', 'destinations', 'resort', 'resorts', 'hotel', 'hotels',
            'motel', 'motels', 'inn', 'inns', 'lodge', 'lodges', 'cabin', 'cabins', 'villa',
            'villas', 'apartment', 'apartments', 'condo', 'condos', 'rental', 'rentals',
            'booking', 'bookings', 'reservation', 'reservations', 'package', 'packages',
            'deal', 'deals', 'discount', 'discounts', 'sale', 'sales', 'special offer',
            'limited time offer', 'exclusive offer', 'member discount', 'loyalty program',
            'frequent flyer', 'miles', 'points', 'rewards', 'bonus', 'bonuses', 'free',
            'complimentary', 'included', 'all inclusive', 'all-inclusive', 'luxury', 'deluxe',
            'premium', 'first class', 'business class', 'economy class', 'flight', 'flights',
            'airline', 'airlines', 'airport', 'airports', 'cruise', 'cruises', 'cruise ship',
            'cruise line', 'cruise lines', 'sailing', 'yacht', 'yachts', 'boat', 'boats',
            'car rental', 'car rentals', 'rental car', 'rental cars', 'transportation',
        ],
        
        # Education and Course Spam
        'education_courses': [
            'course', 'courses', 'training', 'trainings', 'education', 'educational', 'learn',
            'learning', 'study', 'studying', 'student', 'students', 'teacher', 'teachers',
            'instructor', 'instructors', 'tutor', 'tutors', 'mentor', 'mentors', 'coach',
            'coaches', 'coaching', 'workshop', 'workshops', 'seminar', 'seminars', 'webinar',
            'webinars', 'class', 'classes', 'lesson', 'lessons', 'tutorial', 'tutorials',
            'guide', 'guides', 'manual', 'manuals', 'handbook', 'handbooks', 'ebook',
            'ebooks', 'book', 'books', 'textbook', 'textbooks', 'curriculum', 'curricula',
            'program', 'programs', 'certificate', 'certificates', 'certification', 'certifications',
            'diploma', 'diplomas', 'degree', 'degrees', 'bachelor', 'masters', 'phd', 'doctorate',
            'university', 'universities', 'college', 'colleges', 'school', 'schools', 'academy',
            'academies', 'institute', 'institutes', 'online course', 'online courses', 'distance learning',
            'e-learning', 'elearning', 'virtual learning', 'remote learning', 'self-paced',
            'flexible schedule', 'part-time', 'full-time', 'intensive', 'accelerated',
            'beginner', 'intermediate', 'advanced', 'expert', 'professional', 'specialist',
        ],
        
        # Real Estate Spam
        'real_estate': [
            'real estate', 'property', 'properties', 'house', 'houses', 'home', 'homes',
            'apartment', 'apartments', 'condo', 'condos', 'condominium', 'condominiums',
            'townhouse', 'townhouses', 'villa', 'villas', 'mansion', 'mansions', 'estate',
            'estates', 'land', 'lots', 'lot', 'acre', 'acres', 'square feet', 'sq ft',
            'bedroom', 'bedrooms', 'bathroom', 'bathrooms', 'kitchen', 'kitchens', 'garage',
            'garages', 'basement', 'basements', 'attic', 'attics', 'deck', 'decks', 'patio',
            'patios', 'pool', 'pools', 'swimming pool', 'garden', 'gardens', 'yard', 'yards',
            'fence', 'fences', 'gate', 'gates', 'driveway', 'driveways', 'sidewalk', 'sidewalks',
            'buy', 'buying', 'purchase', 'purchasing', 'sell', 'selling', 'sale', 'sales',
            'rent', 'renting', 'rental', 'rentals', 'lease', 'leasing', 'landlord', 'landlords',
            'tenant', 'tenants', 'renter', 'renters', 'buyer', 'buyers', 'seller', 'sellers',
            'agent', 'agents', 'realtor', 'realtors', 'broker', 'brokers', 'listing', 'listings',
            'market', 'markets', 'market value', 'appraisal', 'appraisals', 'inspection',
            'inspections', 'inspection report', 'closing', 'closings', 'closing costs',
            'down payment', 'mortgage', 'mortgages', 'financing', 'pre-approval', 'pre-approved',
            'interest rate', 'interest rates', 'monthly payment', 'monthly payments',
        ],
        
        # Automotive Spam
        'automotive': [
            'car', 'cars', 'automobile', 'automobiles', 'vehicle', 'vehicles', 'auto', 'autos',
            'truck', 'trucks', 'suv', 'suvs', 'van', 'vans', 'motorcycle', 'motorcycles',
            'bike', 'bikes', 'bicycle', 'bicycles', 'scooter', 'scooters', 'boat', 'boats',
            'rv', 'rvs', 'recreational vehicle', 'recreational vehicles', 'trailer', 'trailers',
            'buy', 'buying', 'purchase', 'purchasing', 'sell', 'selling', 'sale', 'sales',
            'trade', 'trading', 'trade-in', 'trade-ins', 'financing', 'loan', 'loans',
            'lease', 'leasing', 'rental', 'rentals', 'rent', 'renting', 'insurance', 'insurances',
            'warranty', 'warranties', 'extended warranty', 'service', 'services', 'repair',
            'repairs', 'maintenance', 'maintenances', 'oil change', 'oil changes', 'tune-up',
            'tune-ups', 'inspection', 'inspections', 'emissions', 'safety', 'recall', 'recalls',
            'parts', 'accessories', 'upgrade', 'upgrades', 'customization', 'customizations',
            'performance', 'horsepower', 'torque', 'mpg', 'fuel economy', 'gas mileage',
            'hybrid', 'electric', 'electric vehicle', 'electric vehicles', 'ev', 'evs',
            'tesla', 'toyota', 'honda', 'ford', 'chevrolet', 'bmw', 'mercedes', 'audi',
            'nissan', 'hyundai', 'kia', 'mazda', 'subaru', 'volkswagen', 'volvo', 'lexus',
            'acura', 'infiniti', 'cadillac', 'lincoln', 'buick', 'gmc', 'dodge', 'jeep',
            'ram', 'chrysler', 'fiat', 'alfa romeo', 'jaguar', 'land rover', 'mini',
            'porsche', 'ferrari', 'lamborghini', 'mclaren', 'bentley', 'rolls royce',
            'aston martin', 'maserati', 'genesis', 'rivian', 'lucid', 'polestar',
        ],
        
        # Urgency and Pressure Tactics
        'urgency_pressure': [
            'urgent', 'urgently', 'immediate', 'immediately', 'asap', 'as soon as possible',
            'right now', 'today', 'tonight', 'this week', 'this month', 'limited time',
            'limited offer', 'while supplies last', 'first come first served', 'act now',
            'don\'t miss out', 'last chance', 'final chance', 'one time only', 'exclusive',
            'exclusively', 'special', 'specially', 'unique', 'uniquely', 'rare', 'rarely',
            'limited edition', 'collector\'s edition', 'vip', 'premium', 'premium only',
            'members only', 'invitation only', 'by invitation only', 'private', 'privately',
            'confidential', 'confidentially', 'secret', 'secrets', 'insider', 'insiders',
            'exclusive access', 'early access', 'pre-sale', 'pre-order', 'advance order',
            'priority', 'prioritize', 'rush', 'rushed', 'express', 'expedited', 'fast',
            'quick', 'quickly', 'instant', 'instantly', 'immediate', 'immediately',
            'same day', 'next day', 'overnight', '24 hour', '24/7', 'round the clock',
        ],
        
        # Free and Guarantee Claims
        'free_guarantees': [
            'free', 'freedom', 'freedoms', 'complimentary', 'no cost', 'no charge', 'at no cost',
            'at no charge', 'without cost', 'without charge', 'zero cost', 'zero charge',
            'gratis', 'gratuitous', 'gift', 'gifts', 'bonus', 'bonuses', 'extra', 'extras',
            'bonus gift', 'free gift', 'free bonus', 'free trial', 'free sample', 'free samples',
            'free consultation', 'free estimate', 'free quote', 'free shipping', 'free delivery',
            'free installation', 'free setup', 'free training', 'free support', 'free maintenance',
            'guaranteed', 'guarantee', 'guarantees', 'money back guarantee', 'satisfaction guaranteed',
            '100% satisfaction', '100% guaranteed', 'lifetime guarantee', 'full guarantee',
            'complete guarantee', 'total guarantee', 'absolute guarantee', 'unconditional guarantee',
            'no questions asked', 'no risk', 'risk-free', 'no obligation', 'no commitment',
            'no strings attached', 'no fine print', 'no hidden fees', 'no hidden costs',
            'transparent', 'transparency', 'honest', 'honestly', 'trustworthy', 'reliable',
            'dependable', 'proven', 'tested', 'verified', 'certified', 'approved', 'endorsed',
            'recommended', 'recommendation', 'testimonial', 'testimonials', 'review', 'reviews',
            'rating', 'ratings', 'star', 'stars', 'five star', 'five stars', 'top rated',
            'best selling', 'bestseller', 'bestsellers', 'popular', 'trending', 'viral',
        ],
        
        # Contact and Communication
        'contact_communication': [
            'call', 'calls', 'calling', 'phone', 'phones', 'telephone', 'telephones',
            'mobile', 'cell', 'cell phone', 'cell phones', 'smartphone', 'smartphones',
            'text', 'texts', 'texting', 'sms', 'message', 'messages', 'messaging',
            'email', 'emails', 'emailing', 'contact', 'contacts', 'contacting', 'reach',
            'reaching', 'connect', 'connecting', 'connection', 'connections', 'network',
            'networking', 'social', 'social media', 'facebook', 'twitter', 'instagram',
            'linkedin', 'youtube', 'tiktok', 'snapchat', 'whatsapp', 'telegram',
            'discord', 'skype', 'zoom', 'teams', 'meet', 'meeting', 'meetings',
            'conference', 'conferences', 'webinar', 'webinars', 'video call', 'video calls',
            'chat', 'chats', 'chatting', 'live chat', 'support', 'customer support',
            'help', 'helping', 'assistance', 'assist', 'assisting', 'service', 'services',
            'representative', 'representatives', 'agent', 'agents', 'specialist', 'specialists',
            'expert', 'experts', 'professional', 'professionals', 'consultant', 'consultants',
            'advisor', 'advisors', 'coach', 'coaches', 'mentor', 'mentors', 'guide', 'guides',
        ],
        
        # Common Spam Phrases and Patterns
        'spam_phrases': [
            'click here', 'click now', 'click below', 'click the link', 'click the button',
            'visit now', 'visit today', 'visit our website', 'go to', 'check out', 'see more',
            'learn more', 'find out more', 'discover more', 'get started', 'get started now',
            'get started today', 'sign up', 'sign up now', 'sign up today', 'register now',
            'register today', 'join now', 'join today', 'become a member', 'membership',
            'subscribe', 'subscription', 'newsletter', 'newsletters', 'updates', 'alerts',
            'notifications', 'reminders', 'follow us', 'like us', 'share', 'sharing',
            'recommend', 'recommendation', 'refer', 'referral', 'referrals', 'invite',
            'invitation', 'invitations', 'spread the word', 'tell your friends', 'share with friends',
            'forward to friends', 'send to friends', 'pass it on', 'don\'t keep this to yourself',
            'this is too good to keep secret', 'you won\'t believe this', 'this will change your life',
            'this is amazing', 'incredible', 'unbelievable', 'shocking', 'surprising',
            'you need to see this', 'you have to try this', 'everyone is talking about this',
            'this is going viral', 'trending now', 'hot topic', 'breaking news', 'urgent news',
            'important announcement', 'special announcement', 'exclusive news', 'insider news',
            'confidential information', 'private information', 'sensitive information',
            'classified information', 'restricted information', 'for your eyes only',
        ]
    }
    
    # Flatten all categories into a single list
    all_spam_keywords = []
    for category, keywords in spam_keywords.items():
        all_spam_keywords.extend(keywords)
    
    # Remove duplicates and sort
    unique_spam_keywords = sorted(list(set(all_spam_keywords)))
    
    return unique_spam_keywords, spam_keywords

def generate_spam_patterns():
    """
    Generate additional spam patterns and regex patterns.
    """
    spam_patterns = [
        # Financial patterns
        (r'\b(?:earn|make|get)\s+\$\d+(?:,\d{3})*(?:\.\d{2})?\s+(?:per|every)\s+(?:day|week|month|year)\b', 'Money-making claims', 25),
        (r'\b(?:guaranteed|promised)\s+\$\d+(?:,\d{3})*(?:\.\d{2})?\s+(?:return|profit|income)\b', 'Guaranteed returns', 30),
        (r'\b(?:no\s+risk|risk-free|zero\s+risk)\s+(?:investment|trading|opportunity)\b', 'Risk-free claims', 20),
        (r'\b(?:work\s+from\s+home|home\s+based|remote\s+work)\s+(?:job|business|opportunity)\b', 'Work-from-home scams', 18),
        (r'\b(?:passive\s+income|residual\s+income|recurring\s+income)\b', 'Passive income claims', 15),
        
        # Urgency patterns
        (r'\b(?:act\s+now|don\'t\s+miss\s+out|last\s+chance|limited\s+time)\b', 'Urgency tactics', 15),
        (r'\b(?:while\s+supplies\s+last|first\s+come\s+first\s+served|one\s+time\s+only)\b', 'Scarcity tactics', 15),
        (r'\b(?:exclusive|invitation\s+only|members\s+only|vip\s+only)\b', 'Exclusivity claims', 12),
        (r'\b(?:urgent|immediate|asap|right\s+now)\b', 'Urgency spam', 10),
        
        # Free and guarantee patterns
        (r'\b(?:100%|completely|totally|absolutely)\s+(?:free|guaranteed|risk-free)\b', 'Absolute claims', 15),
        (r'\b(?:no\s+obligation|no\s+commitment|no\s+strings\s+attached)\b', 'No-obligation claims', 12),
        (r'\b(?:money\s+back\s+guarantee|satisfaction\s+guaranteed)\b', 'Guarantee claims', 15),
        (r'\b(?:free\s+(?:trial|sample|gift|bonus|consultation))\b', 'Free offers', 10),
        
        # Contact and action patterns
        (r'\b(?:call\s+now|text\s+now|email\s+now|contact\s+us\s+now)\b', 'Contact urgency', 12),
        (r'\b(?:click\s+(?:here|now|below|the\s+link))\b', 'Click urgency', 10),
        (r'\b(?:visit\s+(?:now|today|our\s+website))\b', 'Visit urgency', 10),
        (r'\b(?:sign\s+up\s+(?:now|today|immediately))\b', 'Sign-up urgency', 10),
        
        # Social proof patterns
        (r'\b(?:everyone\s+is\s+(?:doing|using|buying|trying))\b', 'Social proof claims', 15),
        (r'\b(?:thousands\s+of\s+(?:people|customers|users|members))\b', 'Large number claims', 12),
        (r'\b(?:join\s+(?:thousands|millions)\s+of\s+(?:people|customers|users))\b', 'Join claims', 12),
        (r'\b(?:don\'t\s+be\s+left\s+behind|don\'t\s+miss\s+out)\b', 'FOMO tactics', 15),
        
        # Health and medical patterns
        (r'\b(?:miracle\s+(?:cure|treatment|solution|remedy))\b', 'Miracle claims', 20),
        (r'\b(?:lose\s+\d+\s+(?:pounds|lbs|kg)\s+(?:in|per)\s+\d+\s+(?:days|weeks|months)\b', 'Weight loss claims', 18),
        (r'\b(?:cure\s+(?:for|of)\s+(?:cancer|diabetes|arthritis|depression))\b', 'Disease cure claims', 25),
        (r'\b(?:doctor\s+(?:recommended|approved|endorsed))\b', 'Medical endorsement claims', 15),
        
        # Technology patterns
        (r'\b(?:virus\s+(?:detected|found|removed|cleaned))\b', 'Virus claims', 15),
        (r'\b(?:system\s+(?:infected|compromised|at\s+risk))\b', 'System threat claims', 15),
        (r'\b(?:update\s+(?:required|needed|immediately))\b', 'Update urgency', 12),
        (r'\b(?:security\s+(?:breach|threat|alert|warning))\b', 'Security claims', 15),
        
        # Dating and relationship patterns
        (r'\b(?:single\s+(?:women|men|people)\s+(?:in|near|around))\b', 'Dating location claims', 12),
        (r'\b(?:find\s+(?:love|your\s+soulmate|the\s+one))\b', 'Love claims', 10),
        (r'\b(?:guaranteed\s+(?:date|match|relationship))\b', 'Dating guarantees', 15),
        (r'\b(?:thousands\s+of\s+(?:single|available)\s+(?:women|men|people))\b', 'Dating pool claims', 12),
    ]
    
    return spam_patterns

def main():
    """
    Main function to generate comprehensive spam keywords.
    """
    print("=" * 60)
    print("COMPREHENSIVE SPAM KEYWORDS GENERATOR")
    print("=" * 60)
    
    # Generate spam keywords
    print("Generating comprehensive spam keywords...")
    spam_keywords, categorized_keywords = generate_comprehensive_spam_keywords()
    
    print(f"Total spam keywords generated: {len(spam_keywords)}")
    
    # Show category breakdown
    print("\nCategory breakdown:")
    for category, keywords in categorized_keywords.items():
        print(f"  {category.replace('_', ' ').title()}: {len(keywords)} keywords")
    
    # Generate spam patterns
    print("\nGenerating spam patterns...")
    spam_patterns = generate_spam_patterns()
    print(f"Total spam patterns generated: {len(spam_patterns)}")
    
    # Save to file
    output_file = "comprehensive_spam_keywords.py"
    print(f"\nSaving to: {output_file}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write('Comprehensive Spam Keywords List\n')
        f.write('Generated by generate_spam_keywords.py\n')
        f.write('"""\n\n')
        
        f.write('# COMPREHENSIVE SPAM KEYWORDS LIST\n')
        f.write('SPAM_KEYWORDS = [\n')
        for keyword in spam_keywords:
            f.write(f'    "{keyword}",\n')
        f.write(']\n\n')
        
        f.write('# SPAM PATTERNS (regex patterns with descriptions and scores)\n')
        f.write('SPAM_PATTERNS = [\n')
        for pattern, description, score in spam_patterns:
            f.write(f'    (r"{pattern}", "{description}", {score}),\n')
        f.write(']\n\n')
        
        f.write('# CATEGORIZED SPAM KEYWORDS\n')
        f.write('SPAM_KEYWORDS_BY_CATEGORY = {\n')
        for category, keywords in categorized_keywords.items():
            f.write(f'    "{category}": [\n')
            for keyword in keywords:
                f.write(f'        "{keyword}",\n')
            f.write('    ],\n')
        f.write('}\n')
    
    print(f"Saved {len(spam_keywords)} spam keywords and {len(spam_patterns)} patterns")
    
    # Also save a human-readable version
    human_readable_file = "spam_keywords_readable.txt"
    with open(human_readable_file, 'w', encoding='utf-8') as f:
        f.write("# Comprehensive Spam Keywords List\n")
        f.write("# Generated by generate_spam_keywords.py\n\n")
        
        for category, keywords in categorized_keywords.items():
            f.write(f"# {category.replace('_', ' ').title()}\n")
            f.write("# " + "=" * 50 + "\n")
            for keyword in sorted(keywords):
                f.write(f'"{keyword}",\n')
            f.write("\n")
    
    print(f"Human-readable version saved to: {human_readable_file}")
    
    print("\n" + "=" * 60)
    print("SPAM KEYWORDS GENERATION COMPLETE!")
    print("=" * 60)
    print(f"Total keywords: {len(spam_keywords)}")
    print(f"Total patterns: {len(spam_patterns)}")
    print(f"Categories: {len(categorized_keywords)}")

if __name__ == "__main__":
    main()
