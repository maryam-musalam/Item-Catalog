# sqlalcmey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, Categories, ElectronicItems, User

engine = create_engine(
                       'sqlite:///electronic.db?check_same_thread=False'
                       )

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
User1 = User(name="Mariam Musalam",
             email="maryam-musalam@hotmail.com",
             image='avatar.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
category1 = Categories(user_id=1,
                       name="Phones",
                       image="phones.jpg")

session.add(category1)
session.commit()

electronic_items1 = ElectronicItems(user_id=1,
                                    name="iphone 5",
                                    description="Capacity - 32 GB , Display: \
                                    Size- 4 \", Camera Resolution \
                                    - Rear: 12 MP / Front: 1.2 MP \
                                    ,Processor Cores - Dual Core , \
                                    Battery Capacity- 1642 mAh , \
                                    Product Type - Smartphone , Operating \
                                    System - iOS 11 , Supported \
                                    Network - 4G LTE  ",
                                    price="SR999",
                                    image="iphone5.jpg", categories=category1)

session.add(electronic_items1)
session.commit()


electronic_items2 = ElectronicItems(user_id=1,
                                    name="iphone 6",
                                    description="Highlights :Metal body \
                                    armoured with ion strengthened \
                                    glass and oleophobic\
                                    coating enhances durability. Retina HD \
                                    display provides a stunning visual \
                                    experience.\
                                    Swipe gestures designed to seamlessly \
                                    navigate the phone with one hand \
                                    ,M8 motion co-processor\
                                    efficiently gathers data from advanced\
                                    sensors and a new barometer",
                                    price="SAR 1139.00",
                                    image="iphone6.jpg",
                                    categories=category1)

session.add(electronic_items2)
session.commit()


electronic_items3 = ElectronicItems(user_id=1,
                                    name="iphone 8",
                                    description="iPhone 8 Plus introduces \
                                    an all new glass design. The worlds \
                                    most popular camera, now even better \
                                    The smartest, most powerful chip ever \
                                    in a smartphone. Wireless charging \
                                    thats truly effortless. And augmented \
                                    reality experiences never before \
                                    possible.iPhone 8 Plus. \
                                    A new generation of iPhone.",
                                    price="SAR 3699.00",
                                    image="iphone8.jpg",
                                    categories=category1)

session.add(electronic_items3)
session.commit()


category2 = Categories(user_id=1,
                       name="Laptops",
                       image="laptops.jpg")

session.add(category2)
session.commit()

electronic_items1 = ElectronicItems(
                                    user_id=1,
                                    name="MacBook Air 13.3-inch",
                                    description="Thin, light, powerful, \
                                    and elegant device,Two thunderbolt 3 \
                                    ports for some powerfull connectivity ,\
                                    Intel core i5 Processor and 8 GB \
                                    RAM ensures high processing \
                                    speed and efficient multitasking,128 \
                                    gb SSD for storing and accessing \
                                    the data with speed",
                                    price="SAR 4898.00",
                                    image="MacBookAir13.jpg",
                                    categories=category2
                                    )

session.add(electronic_items1)
session.commit()


electronic_items2 = ElectronicItems(
                                    user_id=1,
                                    name="Acer - EXTENSE 15 EX2519 -C4U0",
                                    description="Smoothly and quickly \
                                    view and edit large spreadsheets, \
                                    presentations and video \
                                    with higher performance lower \
                                    power DDR4 memory of up to 16GB \
                                    Maintain a strong, consistent \
                                    Internet connection with Gigabit \
                                    Ethernet and 802.11ac wireless antenna\
                                    Shaped for comfort and style, \
                                    the chiclet keyboard stands out \
                                    with its round-cornered \
                                    keys and 1.6mm travel Expand \
                                    functionality with the plethora \
                                    of ports to connect \
                                    almost any secondary device",
                                    price="SAR 859.00",
                                    image="Model2.jpg",
                                    categories=category2
                                    )

session.add(electronic_items2)
session.commit()


electronic_items3 = ElectronicItems(
                                    user_id=1,
                                    name="iLife -IL.1406G.232WAS",
                                    description="Intel Atom processor \
                                    strikes a fine balance between \
                                    optimal performance\
                                    and battery life 2GB RAM allows\
                                    multitasking without device lag \
                                    The 14-Inch display provides \
                                    multimedia experience by producing \
                                    vibrant colours \
                                    and sharp contrast Integrated \
                                    graphics enriches high-end \
                                    gaming experience \
                                    The high capacity battery ensures \
                                    prolonged hours of computing",
                                    price="SAR 523.95",
                                    image="laptop3.jpg",
                                    categories=category2
                                    )

session.add(electronic_items3)
session.commit()


category3 = Categories(user_id=1,
                       name="Tablets",
                       image="lapyop.jpg")

session.add(category3)
session.commit()


electronic_items1 = ElectronicItems(
                                    user_id=1,
                                    name="Yoga Tab 3 850F Tablet 16GB",
                                    description="Touchscreen display, \
                                    Portable, Windows",
                                    price="SAR 799.00",
                                    image="Yoga.jpg",
                                    categories=category3
                                    )

session.add(electronic_items1)
session.commit()


electronic_items2 = ElectronicItems(user_id=1,
                                    name="Original Box CHUWI Hi9 Air ",
                                    description="Android 8.0 System\
                                    The new Android 8.0 OS decreases \
                                    mounts of storage space required\
                                    for apps and improves runtime \
                                    device performance.",
                                    price="SR999",
                                    image="tablet2.jpg",
                                    categories=category3)

session.add(electronic_items2)
session.commit()


category4 = Categories(user_id=1,
                       name="Accessories",
                       image="accessory.jpg")

session.add(category4)
session.commit()


electronic_items1 = ElectronicItems(
                                    user_id=1,
                                    name="QuietComfort 35 Series II",
                                    description="Noise-rejecting \
                                    dual-microphone \
                                    system for clear phone calls and voice\
                                    access to your phone's default \
                                    virtual assistant, like Siri \
                                    Industry-leading wireless headphones \
                                    let you adjust the level of noise \
                                    cancellation to suit your environment \
                                    Volume-optimized EQ makes your music \
                                    always sounds its best, whether you \
                                    turn it up on an airplane, or turn\
                                    it down while at the office",
                                    price="SAR 1296.00",
                                    image="Bose.jpg",
                                    categories=category4
                                    )

session.add(electronic_items1)
session.commit()


electronic_items2 = ElectronicItems(
                                    user_id=1,
                                    name="1.5 Meter Micro USB Charging \
                                    Cable Braided",
                                    description="Imparts hassle free and \
                                    efficient charging \
                                    Made from high quality material that \
                                    provides high resilience and durability \
                                    Bending cable imparts no damage or \
                                    change in performance Features super \
                                    speed syncing capacity and transfers \
                                    data to and from all your devices at \
                                    speed of up to 480 Mbp Revolutionary \
                                    cable for charging power and \
                                    transferring data simultaneously",
                                    price="SAR 15.00",
                                    image="cord.jpg",
                                    categories=category4
                                    )

session.add(electronic_items2)
session.commit()

print "added menu items!"
