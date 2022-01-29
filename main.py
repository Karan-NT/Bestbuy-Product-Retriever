import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import time

l = '''
<div class="productItemRow_hyNOs row_1mOdd"><div class="col-xs-4_1EA1G col-sm-12_G_a2r productItemImageContainer_3qUiK productImgMarginRight_1NXDl"><div class="productImageContainer_1V2HD touchActionManipulation_31CMi productItemImage_1en8J applyResponsiveSquareTrick_35RAF" data-automation="image-slider-test"><div><div class="displayingImage_3xp0y"><div class="sliderTarget_2Q87g"></div><img class="productItemImage_1en8J" src="https://multimedia.bbycastatic.ca/multimedia/products/250x250/105/10562/10562658.png" srcset="https://multimedia.bbycastatic.ca/multimedia/products/500x500/105/10562/10562658.png 3x" alt="Asus GeForce GTX 1050 Ti 4GB Phoenix Fan Edition DVI-D HDMI DP 1.4 Gaming Graphics Card (PH-GTX1050TI-4G) Graphic Cards" itemprop="image"></div></div></div></div><div class="col-xs-8_1v0z0 col-sm-12_G_a2r productItemTextContainer_HocvR"><div class="productItemName_3IZ3c" itemprop="name" data-automation="productItemName">Asus GeForce GTX 1050 Ti 4GB Phoenix Fan Edition DVI-D HDMI DP 1.4 Gaming Graphics Card (PH-GTX1050TI-4G) Graphic Cards</div><div class="ratingContainer_29ZF-"><div class="starRateContainer_3dnAH" role="button"><div class="feedbackStarContainer_2eC1W"><div class="ratableStar_3ea3F"><svg viewBox="0 0 32 32" class="emptyStar_1G0Fx"><path d="M16 23.21l7.13 4.13-1.5-7.62a.9.9 0 0 1 .27-.83l5.64-5.29-7.64-.93a.9.9 0 0 1-.71-.52L16 5.1l-3.22 7a.9.9 0 0 1-.71.52l-7.6.93 5.63 5.29a.9.9 0 0 1 .27.83l-1.51 7.67zm0 2l-7.9 4.58a.9.9 0 0 1-1.34-.95l1.73-9-6.65-6.3A.9.9 0 0 1 2.36 12l9-1.08 3.81-8.32a.9.9 0 0 1 1.64 0l3.81 8.32 9 1.08a.9.9 0 0 1 .51 1.55l-6.66 6.3 1.68 9a.9.9 0 0 1-1.34.94z" fill="#c5cad4" fill-rule="evenodd"></path></svg><div class="partialStar_1Zt5f" style="width: 100%;"><svg class="icon_q2ZYd fullStar_365cI" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 25.19l-8.24 4.65a.9.9 0 0 1-1.33-1l1.8-9-6.86-6.26A.9.9 0 0 1 1.88 12l9.32-1.08 4-8.39a.9.9 0 0 1 1.63 0l4 8.39L30.12 12a.9.9 0 0 1 .5 1.56l-6.88 6.29 1.74 9a.9.9 0 0 1-1.33 1z" fill="#fecf0a" fill-rule="evenodd"></path></svg></div></div><div class="ratableStar_3ea3F"><svg viewBox="0 0 32 32" class="emptyStar_1G0Fx"><path d="M16 23.21l7.13 4.13-1.5-7.62a.9.9 0 0 1 .27-.83l5.64-5.29-7.64-.93a.9.9 0 0 1-.71-.52L16 5.1l-3.22 7a.9.9 0 0 1-.71.52l-7.6.93 5.63 5.29a.9.9 0 0 1 .27.83l-1.51 7.67zm0 2l-7.9 4.58a.9.9 0 0 1-1.34-.95l1.73-9-6.65-6.3A.9.9 0 0 1 2.36 12l9-1.08 3.81-8.32a.9.9 0 0 1 1.64 0l3.81 8.32 9 1.08a.9.9 0 0 1 .51 1.55l-6.66 6.3 1.68 9a.9.9 0 0 1-1.34.94z" fill="#c5cad4" fill-rule="evenodd"></path></svg><div class="partialStar_1Zt5f" style="width: 100%;"><svg class="icon_q2ZYd fullStar_365cI" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 25.19l-8.24 4.65a.9.9 0 0 1-1.33-1l1.8-9-6.86-6.26A.9.9 0 0 1 1.88 12l9.32-1.08 4-8.39a.9.9 0 0 1 1.63 0l4 8.39L30.12 12a.9.9 0 0 1 .5 1.56l-6.88 6.29 1.74 9a.9.9 0 0 1-1.33 1z" fill="#fecf0a" fill-rule="evenodd"></path></svg></div></div><div class="ratableStar_3ea3F"><svg viewBox="0 0 32 32" class="emptyStar_1G0Fx"><path d="M16 23.21l7.13 4.13-1.5-7.62a.9.9 0 0 1 .27-.83l5.64-5.29-7.64-.93a.9.9 0 0 1-.71-.52L16 5.1l-3.22 7a.9.9 0 0 1-.71.52l-7.6.93 5.63 5.29a.9.9 0 0 1 .27.83l-1.51 7.67zm0 2l-7.9 4.58a.9.9 0 0 1-1.34-.95l1.73-9-6.65-6.3A.9.9 0 0 1 2.36 12l9-1.08 3.81-8.32a.9.9 0 0 1 1.64 0l3.81 8.32 9 1.08a.9.9 0 0 1 .51 1.55l-6.66 6.3 1.68 9a.9.9 0 0 1-1.34.94z" fill="#c5cad4" fill-rule="evenodd"></path></svg><div class="partialStar_1Zt5f" style="width: 100%;"><svg class="icon_q2ZYd fullStar_365cI" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 25.19l-8.24 4.65a.9.9 0 0 1-1.33-1l1.8-9-6.86-6.26A.9.9 0 0 1 1.88 12l9.32-1.08 4-8.39a.9.9 0 0 1 1.63 0l4 8.39L30.12 12a.9.9 0 0 1 .5 1.56l-6.88 6.29 1.74 9a.9.9 0 0 1-1.33 1z" fill="#fecf0a" fill-rule="evenodd"></path></svg></div></div><div class="ratableStar_3ea3F"><svg viewBox="0 0 32 32" class="emptyStar_1G0Fx"><path d="M16 23.21l7.13 4.13-1.5-7.62a.9.9 0 0 1 .27-.83l5.64-5.29-7.64-.93a.9.9 0 0 1-.71-.52L16 5.1l-3.22 7a.9.9 0 0 1-.71.52l-7.6.93 5.63 5.29a.9.9 0 0 1 .27.83l-1.51 7.67zm0 2l-7.9 4.58a.9.9 0 0 1-1.34-.95l1.73-9-6.65-6.3A.9.9 0 0 1 2.36 12l9-1.08 3.81-8.32a.9.9 0 0 1 1.64 0l3.81 8.32 9 1.08a.9.9 0 0 1 .51 1.55l-6.66 6.3 1.68 9a.9.9 0 0 1-1.34.94z" fill="#c5cad4" fill-rule="evenodd"></path></svg><div class="partialStar_1Zt5f" style="width: 100%;"><svg class="icon_q2ZYd fullStar_365cI" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 25.19l-8.24 4.65a.9.9 0 0 1-1.33-1l1.8-9-6.86-6.26A.9.9 0 0 1 1.88 12l9.32-1.08 4-8.39a.9.9 0 0 1 1.63 0l4 8.39L30.12 12a.9.9 0 0 1 .5 1.56l-6.88 6.29 1.74 9a.9.9 0 0 1-1.33 1z" fill="#fecf0a" fill-rule="evenodd"></path></svg></div></div><div class="ratableStar_3ea3F"><svg viewBox="0 0 32 32" class="emptyStar_1G0Fx"><path d="M16 23.21l7.13 4.13-1.5-7.62a.9.9 0 0 1 .27-.83l5.64-5.29-7.64-.93a.9.9 0 0 1-.71-.52L16 5.1l-3.22 7a.9.9 0 0 1-.71.52l-7.6.93 5.63 5.29a.9.9 0 0 1 .27.83l-1.51 7.67zm0 2l-7.9 4.58a.9.9 0 0 1-1.34-.95l1.73-9-6.65-6.3A.9.9 0 0 1 2.36 12l9-1.08 3.81-8.32a.9.9 0 0 1 1.64 0l3.81 8.32 9 1.08a.9.9 0 0 1 .51 1.55l-6.66 6.3 1.68 9a.9.9 0 0 1-1.34.94z" fill="#c5cad4" fill-rule="evenodd"></path></svg><div class="partialStar_1Zt5f" style="width: 40%;"><svg class="icon_q2ZYd fullStar_365cI" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 25.19l-8.24 4.65a.9.9 0 0 1-1.33-1l1.8-9-6.86-6.26A.9.9 0 0 1 1.88 12l9.32-1.08 4-8.39a.9.9 0 0 1 1.63 0l4 8.39L30.12 12a.9.9 0 0 1 .5 1.56l-6.88 6.29 1.74 9a.9.9 0 0 1-1.33 1z" fill="#fecf0a" fill-rule="evenodd"></path></svg></div></div></div><div class="reviews_1KIjQ"><span class="reviewCountContainer_2EO6o" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating"><meta itemprop="ratingValue" content="4.36"><meta itemprop="reviewCount" content="11"><span data-automation="rating-count">(11 Reviews)</span></span></div></div></div><div class="productPricingContainer_3gTS3" data-automation="product-pricing"><span class="" data-automation="product-price"><span class="screenReaderOnly_3anTj large_3aP7Z">$359.99</span><div class="price_FHDfG medium_za6t1 " aria-hidden="true">$359.99</div></span></div><div class="availabilityMessageSearch_1KfqF" data-automation="store-availability-messages"><p class="shippingAvailability_2X3xt"><span data-automation="store-availability-checkmark" aria-hidden="true"><svg class="green_2_vro icon_DeHIB iconStyle_H9oNs icon_q2ZYd" viewBox="0 0 32 32"><path d="M12.22,24.64a.94.94,0,0,1-1.34,0L4.07,17.69a1,1,0,0,1,0-1.37.93.93,0,0,1,1.34,0l6.17,6.25,15-15.21a.93.93,0,0,1,1.34,0,1,1,0,0,1,0,1.36Z"></path></svg></span><span class="container_1DAvI">Available online only</span></p></div><div class="soldAndShippedBy_319gh" id="MarketplaceSeller"><svg class="blue_2GwtG icon_q2ZYd marketplaceLogo_14OwV" viewBox="0 0 64.39 68.36"><path d="M54.26,16.87a2.32,2.32,0,0,1-2.32-2.31,9.94,9.94,0,1,0-19.87,0,2.31,2.31,0,1,1-4.62,0,14.56,14.56,0,0,1,29.12,0A2.32,2.32,0,0,1,54.26,16.87Z" transform="translate(-3.58)"></path><path d="M13.17,16.87a2.31,2.31,0,0,1-2.31-2.31A14.57,14.57,0,0,1,25.41,0a14.79,14.79,0,0,1,2.74.26A2.32,2.32,0,0,1,30,3,2.33,2.33,0,0,1,27.28,4.8a9.72,9.72,0,0,0-1.87-.18,10,10,0,0,0-9.93,9.94A2.32,2.32,0,0,1,13.17,16.87Z" transform="translate(-3.58)"></path><path d="M18.72,19.61a3.48,3.48,0,0,0-3.48,3.47l-.07,36.3c0,1.49.34,3.29,2.59,6s3.16,3,5.59,3H64.43a3.47,3.47,0,0,0,3.47-3.47L68,23a3.46,3.46,0,0,0-3.46-3.47Z" transform="translate(-3.58)"></path><path d="M6.66,19.56a3.3,3.3,0,0,0-3,3.53L3.58,67.52c0,.93.49,1.11,1.1.4L7.36,64.8a8.93,8.93,0,0,0,2.29-6.2V21.25A1.69,1.69,0,0,0,8,19.56Z" transform="translate(-3.58)"></path></svg><span class="marketplaceName_3FG8H">Marketplace seller</span></div></div></div>
'''
print(BeautifulSoup.prettify(BeautifulSoup(l, 'html.parser')))

dataURL = input('\nENTER URL: ')
print('\nRETRIEVING HTML...')

dataRequest = urllib.request.Request(
    dataURL, 
    headers = {'User-Agent': 'Mozilla/5.0'}
)
dataOpen = urllib.request.urlopen(dataRequest).read()
data = BeautifulSoup(dataOpen, 'html.parser')
print('\nRETRIEVAL SUCCESSFUL\n\nRETRIEVING PRODUCTS...')

li = list()
products = dict()
for tag in data.find_all('div'):
    try: tag.get('class')
    except: continue

    if ( (type(tag.get('class'))) == type(li) and 
        'productItemName_3IZ3c' in tag.get('class')
    ):
        pass
    else: continue
    
    print(BeautifulSoup.prettify(tag.parent.parent))
    input('a')

    for child in tag.parent.parent.find_all('span'):
        try: child.get('class')
        except: continue

        if ( (type(child.get('class'))) == type(li) and 
            'container_1DAvI' in child.get('class')
        ):
            print(type(child.get('class')))
            products[tag.text] = child.text

print('\nRETRIEVAL SUCCESSFUL\n\n', products)