import os
pwd = os.getcwd()
os.chdir("..")
from database_setup import db, Company, Phone
os.chdir(pwd)

Apple = Company(id='1', name='Apple', discp='''Apple Inc. is an American
 multinational technology company headquartered in Cupertino, California that
 designs, develops, and sells consumer electronics, computer software, and
 online services.''')

Sony = Company(id='2', name='Sony', discp='''Sony Corporation is a Japanese
 multinational conglomerate corporation headquartered in Konan, Minato, Tokyo.
 Its diversified business includes consumer and professional electronics,
 gaming, entertainment and financial services.''')

Samsung = Company(id='3', name='Samsung', discp='''Samsung Group is a South
 Korean multinational conglomerate headquartered in Samsung Town, Seoul.
 It comprises numerous affiliated businesses, most of them united under the
 Samsung brand, and is the largest South Korean business conglomerate.''')

HTC = Company(id='4', name='HTC', discp='''HTC Corporation is a Taiwanese
 consumer electronics company headquartered in Xindian District, New Taipei
 City, Taiwan. Founded in 1997, HTC began as an original design manufacturer 
 and original equipment manufacturer, designing and manufacturing laptop 
 computers. They re-entered the market in 2008, turning to devices such as
 mobile phones and tablets, releasing their first Smartphone, the HTC Dream.''')

Google = Company(id='5', name='Google', discp='''Google LLC is an American
 multinational technology company that specializes in Internet-related services
 and products. These include online advertising technologies, search,
 cloud computing, software, and hardware. Google was founded in 1998 by Larry
 Page and Sergey Brin while they were Ph.D. students at Stanford University,
 in California. Together, they own about 14 percent of its shares, and control
 56 percent of the stockholder voting power through supervoting stock.''')


db.session.add(Apple)
db.session.add(Sony)
db.session.add(Samsung)
db.session.add(HTC)
db.session.add(Google)
db.session.commit()

iphonex = Phone(id='1', name='iPhone X', specs='''The Apple iPhone X is powered
 by hexa-core Apple A11 Bionic processor and it comes with 3GB of RAM.
 The phone packs 64GB of internal storage that cannot be expanded.
 As far as the cameras are concerned, the Apple iPhone X packs a 12-megapixel
 primary camera on the rear and a 7-megapixel front shooter for selfies''',
                price='85022', rating='92', company_id='1')

iphone8s = Phone(id='2', name='iPhone 8s', specs='''The Apple iPhone 8 is
 powered by hexa-core Apple A11 Bionic processor and it comes with 2GB of RAM.
 The phone packs 64GB of internal storage that cannot be expanded. As far as
 the cameras are concerned, the Apple iPhone 8 packs a 12-megapixel primary
 camera on the rear and a 7-megapixel front shooter for selfies.''',
                 price='54890', rating='90', company_id='1')

xperiaxz1 = Phone(id='3', name='Xperia XZ1', specs='''Qualcomm Snapdragon 835.
 It comes with 4GB of RAM. The phone packs 64GB of internal storage that can be
 expanded up to 256GB via a microSD card. As far as the cameras are concerned,
 the Sony Xperia XZ1 packs a 19-megapixel primary camera on the rear and a
 13-megapixel front shooter for selfies.''',
                price='44990', rating='93', company_id='2')

xperiaxzpremium = Phone(id='4', name='Xperia XZ Premium', specs='''The Sony
 Xperia XZ Premium is powered by octa-core Qualcomm Snapdragon 835 processor
 and it comes with 4GB of RAM. The phone packs 64GB of internal storage that
 can be expanded up to 256GB via a microSD card. As far as the cameras are
 concerned, the Sony Xperia XZ Premium packs a 19-megapixel primary camera on
 the rear and a 13-megapixel front shooter for selfies.''',
                        price='55735', rating='80', company_id='2')

galaxys8 = Phone(id='5', name='Samsung Galaxy S8', specs='''The Samsung
 Galaxy S8 is powered by 1.9GHz octa-core Samsung Exynos 8895 processor and it
 comes with 4GB of RAM. The phone packs 64GB of internal storage that can be
 expanded up to 256GB via a microSD card. As far as the cameras are concerned,
 the Samsung Galaxy S8 packs a 12-megapixel primary camera on the rear and a 
 8-megapixel front shooter for selfies.''',
                        price='53990', rating='90', company_id='3')

galaxynote8 = Phone(id='6', name='Samsung Galaxy Note 8', specs='''The
 Samsung Galaxy Note 8 is powered by 1.7GHz octa-core Samsung Exynos 9 Octa
 8895 processor and it comes with 6GB of RAM. The phone packs 64GB of internal
 storage that can be expanded up to 256GB via a microSD card. As far as the
 cameras are concerned, the Samsung Galaxy Note 8 packs a 12-megapixel primary
 camera on the rear and a 8-megapixel front shooter for selfies.''',
                           price='67900', rating='95', company_id='3')

u11 = Phone(id='7', name='HTC U11', specs='''The HTC U11 is powered by
 2.45GHz octa-core Qualcomm Snapdragon 835 processor and it comes with 6GB of
 RAM. The phone packs 128GB of internal storage that can be expanded up to
 2000GB via a microSD card. As far as the cameras are concerned, the HTC U11
 packs a 12-Ultrapixel primary camera on the rear and a 16-megapixel front
 shooter for selfies.''',
               price='48000', rating='89', company_id='4')

onex10 = Phone(id='8', name='HTC One X10', specs='''The HTC One X10 is
 powered by octa-core MediaTek Helio P10 MT6755 processor and it comes with 3GB
 of RAM. The phone packs 32GB of internal storage that can be expanded up to
 200GB via a microSD card. As far as the cameras are concerned, the HTC One X10
 packs a 16-megapixel primary camera on the rear and a 8-megapixel front 
 shooter for selfies.''',
                  price='40000', rating='78', company_id='4')

pixel2xl = Phone(id='9', name='Google Pixel 2 XL', specs='''The Google
 Pixel 2 XL is powered by 1.9GHz octa-core Qualcomm Snapdragon 835 processor
 and it comes with 4GB of RAM. The phone packs 64GB of internal storage that
 cannot be expanded. As far as the cameras are concerned, the Google Pixel 2 XL
 packs a 12.2-megapixel primary camera on the rear and a 8-megapixel front
 shooter for selfies.''',
                       price='67999', rating='96', company_id='5')

pixel2 = Phone(id='10', name='Google Pixel 2', specs='''The Google
 Pixel 2 is powered by 1.9GHz octa-core Qualcomm Snapdragon 835 processor and
 it comes with 4GB of RAM. The phone packs 64GB of internal storage that cannot
 be expanded. As far as the cameras are concerned, the Google Pixel 2 packs a
 12.2-megapixel primary camera on the rear and a 8-megapixel front shooter for
 selfies.''',
                     price='49999', rating='97', company_id='5')

db.session.add(iphonex)
db.session.add(iphone8s)
db.session.add(xperiaxz1)
db.session.add(xperiaxzpremium)
db.session.add(galaxys8)
db.session.add(galaxynote8)
db.session.add(u11)
db.session.add(onex10)
db.session.add(pixel2xl)
db.session.add(pixel2)
db.session.commit()