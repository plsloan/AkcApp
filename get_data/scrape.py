import json
import requests

from bs4 import BeautifulSoup


breeds_links = [
    'https://www.akc.org/dog-breeds/affenpinscher/',
    'https://www.akc.org/dog-breeds/afghan-hound/',
    'https://www.akc.org/dog-breeds/airedale-terrier/',
    'https://www.akc.org/dog-breeds/akita/',
    'https://www.akc.org/dog-breeds/alaskan-malamute/',
    'https://www.akc.org/dog-breeds/american-bulldog/',
    'https://www.akc.org/dog-breeds/american-english-coonhound/',
    'https://www.akc.org/dog-breeds/american-eskimo-dog/',
    'https://www.akc.org/dog-breeds/american-foxhound/',
    'https://www.akc.org/dog-breeds/american-hairless-terrier/',
    'https://www.akc.org/dog-breeds/american-leopard-hound/',
    'https://www.akc.org/dog-breeds/american-staffordshire-terrier/',
    'https://www.akc.org/dog-breeds/american-water-spaniel/',
    'https://www.akc.org/dog-breeds/anatolian-shepherd-dog/',
    'https://www.akc.org/dog-breeds/appenzeller-sennenhund/',
    'https://www.akc.org/dog-breeds/australian-cattle-dog/',
    'https://www.akc.org/dog-breeds/australian-kelpie/',
    'https://www.akc.org/dog-breeds/australian-shepherd/',
    'https://www.akc.org/dog-breeds/australian-stump-tail-cattle-dog/',
    'https://www.akc.org/dog-breeds/australian-terrier/',
    'https://www.akc.org/dog-breeds/azawakh/',
    'https://www.akc.org/dog-breeds/barbet/',
    'https://www.akc.org/dog-breeds/basenji/',
    'https://www.akc.org/dog-breeds/basset-fauve-de-bretagne/',
    'https://www.akc.org/dog-breeds/basset-hound/',
    'https://www.akc.org/dog-breeds/bavarian-mountain-scent-hound/',
    'https://www.akc.org/dog-breeds/beagle/',
    'https://www.akc.org/dog-breeds/bearded-collie/',
    'https://www.akc.org/dog-breeds/beauceron/',
    'https://www.akc.org/dog-breeds/bedlington-terrier/',
    'https://www.akc.org/dog-breeds/belgian-laekenois/',
    'https://www.akc.org/dog-breeds/belgian-malinois/',
    'https://www.akc.org/dog-breeds/belgian-sheepdog/',
    'https://www.akc.org/dog-breeds/belgian-tervuren/',
    'https://www.akc.org/dog-breeds/bergamasco-sheepdog/',
    'https://www.akc.org/dog-breeds/berger-picard/',
    'https://www.akc.org/dog-breeds/bernese-mountain-dog/',
    'https://www.akc.org/dog-breeds/bichon-frise/',
    'https://www.akc.org/dog-breeds/biewer-terrier/',
    'https://www.akc.org/dog-breeds/black-and-tan-coonhound/',
    'https://www.akc.org/dog-breeds/black-russian-terrier/',
    'https://www.akc.org/dog-breeds/bloodhound/',
    'https://www.akc.org/dog-breeds/bluetick-coonhound/',
    'https://www.akc.org/dog-breeds/boerboel/',
    'https://www.akc.org/dog-breeds/bohemian-shepherd/',
    'https://www.akc.org/dog-breeds/bolognese/',
    'https://www.akc.org/dog-breeds/border-collie/',
    'https://www.akc.org/dog-breeds/border-terrier/',
    'https://www.akc.org/dog-breeds/borzoi/',
    'https://www.akc.org/dog-breeds/boston-terrier/',
    'https://www.akc.org/dog-breeds/bouvier-des-flandres/',
    'https://www.akc.org/dog-breeds/boxer/',
    'https://www.akc.org/dog-breeds/boykin-spaniel/',
    'https://www.akc.org/dog-breeds/bracco-italiano/',
    'https://www.akc.org/dog-breeds/braque-du-bourbonnais/',
    'https://www.akc.org/dog-breeds/braque-francais-pyrenean/',
    'https://www.akc.org/dog-breeds/briard/',
    'https://www.akc.org/dog-breeds/brittany/',
    'https://www.akc.org/dog-breeds/broholmer/',
    'https://www.akc.org/dog-breeds/brussels-griffon/',
    'https://www.akc.org/dog-breeds/bull-terrier/',
    'https://www.akc.org/dog-breeds/bulldog/',
    'https://www.akc.org/dog-breeds/bullmastiff/',
    'https://www.akc.org/dog-breeds/cairn-terrier/',
    'https://www.akc.org/dog-breeds/canaan-dog/',
    'https://www.akc.org/dog-breeds/cane-corso/',
    'https://www.akc.org/dog-breeds/cardigan-welsh-corgi/',
    'https://www.akc.org/dog-breeds/carolina-dog/',
    'https://www.akc.org/dog-breeds/catahoula-leopard-dog/',
    'https://www.akc.org/dog-breeds/caucasian-shepherd-dog/',
    'https://www.akc.org/dog-breeds/cavalier-king-charles-spaniel/',
    'https://www.akc.org/dog-breeds/central-asian-shepherd-dog/',
    'https://www.akc.org/dog-breeds/cesky-terrier/',
    'https://www.akc.org/dog-breeds/chesapeake-bay-retriever/',
    'https://www.akc.org/dog-breeds/chihuahua/',
    'https://www.akc.org/dog-breeds/chinese-crested/',
    'https://www.akc.org/dog-breeds/chinese-shar-pei/',
    'https://www.akc.org/dog-breeds/chinook/',
    'https://www.akc.org/dog-breeds/chow-chow/',
    'https://www.akc.org/dog-breeds/cirneco-delletna/',
    'https://www.akc.org/dog-breeds/clumber-spaniel/',
    'https://www.akc.org/dog-breeds/cocker-spaniel/',
    'https://www.akc.org/dog-breeds/collie/',
    'https://www.akc.org/dog-breeds/coton-de-tulear/',
    'https://www.akc.org/dog-breeds/croatian-sheepdog/',
    'https://www.akc.org/dog-breeds/curly-coated-retriever/',
    'https://www.akc.org/dog-breeds/czechoslovakian-vlcak/',
    'https://www.akc.org/dog-breeds/dachshund/',
    'https://www.akc.org/dog-breeds/dalmatian/',
    'https://www.akc.org/dog-breeds/dandie-dinmont-terrier/',
    'https://www.akc.org/dog-breeds/danish-swedish-farmdog/',
    'https://www.akc.org/dog-breeds/deutscher-wachtelhund/',
    'https://www.akc.org/dog-breeds/doberman-pinscher/',
    'https://www.akc.org/dog-breeds/dogo-argentino/',
    'https://www.akc.org/dog-breeds/dogue-de-bordeaux/',
    'https://www.akc.org/dog-breeds/drentsche-patrijshond/',
    'https://www.akc.org/dog-breeds/drever/',
    'https://www.akc.org/dog-breeds/dutch-shepherd/',
    'https://www.akc.org/dog-breeds/english-cocker-spaniel/',
    'https://www.akc.org/dog-breeds/english-foxhound/',
    'https://www.akc.org/dog-breeds/english-setter/',
    'https://www.akc.org/dog-breeds/english-springer-spaniel/',
    'https://www.akc.org/dog-breeds/english-toy-spaniel/',
    'https://www.akc.org/dog-breeds/entlebucher-mountain-dog/',
    'https://www.akc.org/dog-breeds/estrela-mountain-dog/',
    'https://www.akc.org/dog-breeds/eurasier/',
    'https://www.akc.org/dog-breeds/field-spaniel/',
    'https://www.akc.org/dog-breeds/finnish-lapphund/',
    'https://www.akc.org/dog-breeds/finnish-spitz/',
    'https://www.akc.org/dog-breeds/flat-coated-retriever/',
    'https://www.akc.org/dog-breeds/french-bulldog/',
    'https://www.akc.org/dog-breeds/french-spaniel/',
    'https://www.akc.org/dog-breeds/german-longhaired-pointer/',
    'https://www.akc.org/dog-breeds/german-pinscher/',
    'https://www.akc.org/dog-breeds/german-shepherd-dog/',
    'https://www.akc.org/dog-breeds/german-shorthaired-pointer/',
    'https://www.akc.org/dog-breeds/german-spitz/',
    'https://www.akc.org/dog-breeds/german-wirehaired-pointer/',
    'https://www.akc.org/dog-breeds/giant-schnauzer/',
    'https://www.akc.org/dog-breeds/glen-of-imaal-terrier/',
    'https://www.akc.org/dog-breeds/golden-retriever/',
    'https://www.akc.org/dog-breeds/gordon-setter/',
    'https://www.akc.org/dog-breeds/grand-basset-griffon-vendeen/',
    'https://www.akc.org/dog-breeds/great-dane/',
    'https://www.akc.org/dog-breeds/great-pyrenees/',
    'https://www.akc.org/dog-breeds/greater-swiss-mountain-dog/',
    'https://www.akc.org/dog-breeds/greyhound/',
    'https://www.akc.org/dog-breeds/hamiltonstovare/',
    'https://www.akc.org/dog-breeds/hanoverian-scenthound/',
    'https://www.akc.org/dog-breeds/harrier/',
    'https://www.akc.org/dog-breeds/havanese/',
    'https://www.akc.org/dog-breeds/hokkaido/',
    'https://www.akc.org/dog-breeds/hovawart/',
    'https://www.akc.org/dog-breeds/ibizan-hound/',
    'https://www.akc.org/dog-breeds/icelandic-sheepdog/',
    'https://www.akc.org/dog-breeds/irish-red-and-white-setter/',
    'https://www.akc.org/dog-breeds/irish-setter/',
    'https://www.akc.org/dog-breeds/irish-terrier/',
    'https://www.akc.org/dog-breeds/irish-water-spaniel/',
    'https://www.akc.org/dog-breeds/irish-wolfhound/',
    'https://www.akc.org/dog-breeds/italian-greyhound/',
    'https://www.akc.org/dog-breeds/jagdterrier/',
    'https://www.akc.org/dog-breeds/japanese-akitainu/',
    'https://www.akc.org/dog-breeds/japanese-chin/',
    'https://www.akc.org/dog-breeds/japanese-spitz/',
    'https://www.akc.org/dog-breeds/japanese-terrier/',
    'https://www.akc.org/dog-breeds/jindo/',
    'https://www.akc.org/dog-breeds/kai-ken/',
    'https://www.akc.org/dog-breeds/karelian-bear-dog/',
    'https://www.akc.org/dog-breeds/keeshond/',
    'https://www.akc.org/dog-breeds/kerry-blue-terrier/',
    'https://www.akc.org/dog-breeds/kishu-ken/',
    'https://www.akc.org/dog-breeds/komondor/',
    'https://www.akc.org/dog-breeds/kromfohrlander/',
    'https://www.akc.org/dog-breeds/kuvasz/',
    'https://www.akc.org/dog-breeds/labrador-retriever/',
    'https://www.akc.org/dog-breeds/lagotto-romagnolo/',
    'https://www.akc.org/dog-breeds/lakeland-terrier/',
    'https://www.akc.org/dog-breeds/lancashire-heeler/',
    'https://www.akc.org/dog-breeds/lapponian-herder/',
    'https://www.akc.org/dog-breeds/leonberger/',
    'https://www.akc.org/dog-breeds/lhasa-apso/',
    'https://www.akc.org/dog-breeds/lowchen/',
    'https://www.akc.org/dog-breeds/maltese/',
    'https://www.akc.org/dog-breeds/manchester-terrier-standard/',
    'https://www.akc.org/dog-breeds/manchester-terrier-toy/',
    'https://www.akc.org/dog-breeds/mastiff/',
    'https://www.akc.org/dog-breeds/miniature-american-shepherd/',
    'https://www.akc.org/dog-breeds/miniature-bull-terrier/',
    'https://www.akc.org/dog-breeds/miniature-pinscher/',
    'https://www.akc.org/dog-breeds/miniature-schnauzer/',
    'https://www.akc.org/dog-breeds/mountain-cur/',
    'https://www.akc.org/dog-breeds/mudi/',
    'https://www.akc.org/dog-breeds/neapolitan-mastiff/',
    'https://www.akc.org/dog-breeds/nederlandse-kooikerhondje/',
    'https://www.akc.org/dog-breeds/newfoundland/',
    'https://www.akc.org/dog-breeds/norfolk-terrier/',
    'https://www.akc.org/dog-breeds/norrbottenspets/',
    'https://www.akc.org/dog-breeds/norwegian-buhund/',
    'https://www.akc.org/dog-breeds/norwegian-elkhound/',
    'https://www.akc.org/dog-breeds/norwegian-lundehund/',
    'https://www.akc.org/dog-breeds/norwich-terrier/',
    'https://www.akc.org/dog-breeds/nova-scotia-duck-tolling-retriever/',
    'https://www.akc.org/dog-breeds/old-english-sheepdog/',
    'https://www.akc.org/dog-breeds/otterhound/',
    'https://www.akc.org/dog-breeds/papillon/',
    'https://www.akc.org/dog-breeds/parson-russell-terrier/',
    'https://www.akc.org/dog-breeds/pekingese/',
    'https://www.akc.org/dog-breeds/pembroke-welsh-corgi/',
    'https://www.akc.org/dog-breeds/perro-de-presa-canario/',
    'https://www.akc.org/dog-breeds/peruvian-inca-orchid/',
    'https://www.akc.org/dog-breeds/petit-basset-griffon-vendeen/',
    'https://www.akc.org/dog-breeds/pharaoh-hound/',
    'https://www.akc.org/dog-breeds/plott-hound/',
    'https://www.akc.org/dog-breeds/pointer/',
    'https://www.akc.org/dog-breeds/polish-lowland-sheepdog/',
    'https://www.akc.org/dog-breeds/pomeranian/',
    'https://www.akc.org/dog-breeds/poodle-miniature/',
    'https://www.akc.org/dog-breeds/poodle-standard/',
    'https://www.akc.org/dog-breeds/poodle-toy/',
    'https://www.akc.org/dog-breeds/porcelaine/',
    'https://www.akc.org/dog-breeds/portuguese-podengo/',
    'https://www.akc.org/dog-breeds/portuguese-podengo-pequeno/',
    'https://www.akc.org/dog-breeds/portuguese-pointer/',
    'https://www.akc.org/dog-breeds/portuguese-sheepdog/',
    'https://www.akc.org/dog-breeds/portuguese-water-dog/',
    'https://www.akc.org/dog-breeds/pudelpointer/',
    'https://www.akc.org/dog-breeds/pug/',
    'https://www.akc.org/dog-breeds/puli/',
    'https://www.akc.org/dog-breeds/pumi/',
    'https://www.akc.org/dog-breeds/pyrenean-mastiff/',
    'https://www.akc.org/dog-breeds/pyrenean-shepherd/',
    'https://www.akc.org/dog-breeds/rafeiro-do-alentejo/',
    'https://www.akc.org/dog-breeds/rat-terrier/',
    'https://www.akc.org/dog-breeds/redbone-coonhound/',
    'https://www.akc.org/dog-breeds/rhodesian-ridgeback/',
    'https://www.akc.org/dog-breeds/romanian-mioritic-shepherd-dog/',
    'https://www.akc.org/dog-breeds/rottweiler/',
    'https://www.akc.org/dog-breeds/russell-terrier/',
    'https://www.akc.org/dog-breeds/russian-toy/',
    'https://www.akc.org/dog-breeds/russian-tsvetnaya-bolonka/',
    'https://www.akc.org/dog-breeds/st-bernard/',
    'https://www.akc.org/dog-breeds/saluki/',
    'https://www.akc.org/dog-breeds/samoyed/',
    'https://www.akc.org/dog-breeds/schapendoes/',
    'https://www.akc.org/dog-breeds/schipperke/',
    'https://www.akc.org/dog-breeds/scottish-deerhound/',
    'https://www.akc.org/dog-breeds/scottish-terrier/',
    'https://www.akc.org/dog-breeds/sealyham-terrier/',
    'https://www.akc.org/dog-breeds/segugio-italiano/',
    'https://www.akc.org/dog-breeds/shetland-sheepdog/',
    'https://www.akc.org/dog-breeds/shiba-inu/',
    'https://www.akc.org/dog-breeds/shih-tzu/',
    'https://www.akc.org/dog-breeds/shikoku/',
    'https://www.akc.org/dog-breeds/siberian-husky/',
    'https://www.akc.org/dog-breeds/silky-terrier/',
    'https://www.akc.org/dog-breeds/skye-terrier/',
    'https://www.akc.org/dog-breeds/sloughi/',
    'https://www.akc.org/dog-breeds/slovakian-wirehaired-pointer/',
    'https://www.akc.org/dog-breeds/slovensky-cuvac/',
    'https://www.akc.org/dog-breeds/slovensky-kopov/',
    'https://www.akc.org/dog-breeds/small-munsterlander/',
    'https://www.akc.org/dog-breeds/smooth-fox-terrier/',
    'https://www.akc.org/dog-breeds/soft-coated-wheaten-terrier/',
    'https://www.akc.org/dog-breeds/spanish-mastiff/',
    'https://www.akc.org/dog-breeds/spanish-water-dog/',
    'https://www.akc.org/dog-breeds/spinone-italiano/',
    'https://www.akc.org/dog-breeds/stabyhoun/',
    'https://www.akc.org/dog-breeds/staffordshire-bull-terrier/',
    'https://www.akc.org/dog-breeds/standard-schnauzer/',
    'https://www.akc.org/dog-breeds/sussex-spaniel/',
    'https://www.akc.org/dog-breeds/swedish-lapphund/',
    'https://www.akc.org/dog-breeds/swedish-vallhund/',
    'https://www.akc.org/dog-breeds/taiwan-dog/',
    'https://www.akc.org/dog-breeds/teddy-roosevelt-terrier/',
    'https://www.akc.org/dog-breeds/thai-ridgeback/',
    'https://www.akc.org/dog-breeds/tibetan-mastiff/',
    'https://www.akc.org/dog-breeds/tibetan-spaniel/',
    'https://www.akc.org/dog-breeds/tibetan-terrier/',
    'https://www.akc.org/dog-breeds/tornjak/',
    'https://www.akc.org/dog-breeds/tosa/',
    'https://www.akc.org/dog-breeds/toy-fox-terrier/',
    'https://www.akc.org/dog-breeds/transylvanian-hound/',
    'https://www.akc.org/dog-breeds/treeing-tennessee-brindle/',
    'https://www.akc.org/dog-breeds/treeing-walker-coonhound/',
    'https://www.akc.org/dog-breeds/vizsla/',
    'https://www.akc.org/dog-breeds/weimaraner/',
    'https://www.akc.org/dog-breeds/welsh-springer-spaniel/',
    'https://www.akc.org/dog-breeds/welsh-terrier/',
    'https://www.akc.org/dog-breeds/west-highland-white-terrier/',
    'https://www.akc.org/dog-breeds/wetterhoun/',
    'https://www.akc.org/dog-breeds/whippet/',
    'https://www.akc.org/dog-breeds/wire-fox-terrier/',
    'https://www.akc.org/dog-breeds/wirehaired-pointing-griffon/',
    'https://www.akc.org/dog-breeds/wirehaired-vizsla/',
    'https://www.akc.org/dog-breeds/working-kelpie/',
    'https://www.akc.org/dog-breeds/xoloitzcuintli/',
    'https://www.akc.org/dog-breeds/yakutian-laika/',
    'https://www.akc.org/dog-breeds/yorkshire-terrier/'
]


def main():
    breed_data = []
    for link in breeds_links:
        html = requests.get(link).text
        soup = BeautifulSoup(html, features="html.parser")
        breed_data.append(get_breed_data(soup))
    with open('data2.json', 'w') as outfile:
        json.dump(breed_data, outfile)


def get_breed_options(html_text):
    breeds_search = html_text.find('select', {"id": "breed-search"})
    return breeds_search.find_all('option')


def get_breed_links(options):
    links = []
    for opt in options:
        if opt['value'] != '':
            links.append(opt['value'])
    return links


def get_breed_data(html_text):
    breed_name = html_text.find(
        'h1', {'class': 'page-header__title'})

    if breed_name is not None:
        breed_name = breed_name.text.strip()

        breed_attributes = extract_attributes(html_text, breed_name)
        breed_traits = extract_traits(html_text)

        breed_info = {'breed_name': breed_name,
                      'attributes': breed_attributes, 'traits': breed_traits}

        return breed_info
    else:
        return {}


def extract_attributes(html_text, breed_name=None):
    breed_tabs = html_text.find_all('div', {"class": "tabs__tab-panel"})
    breed_attributes = {}
    for tab in breed_tabs:
        attributes = tab.find_all('li', {'class': 'attribute-list__row'})
        for att in attributes:
            term = att.find(
                'span', {'class': 'attribute-list__term'})
            if term is not None:
                term = term.text.split(':')[0]
            else:
                raise Exception('Could not find term for breed: {}.'.format())
            description = att.find(
                'span', {'class': 'attribute-list__description'})
            if description is not None:
                description = description.text
                if term == 'Temperament':
                    description = description.split(', ')
                elif term == 'AKC Breed Popularity':
                    description = [int(i)
                                   for i in description.split() if i.isdigit()][0]
                elif term == 'Height':
                    description = parse_height(description)
                elif term == 'Weight':
                    description = parse_weight(description)
                elif term == 'Life Expectancy':
                    description = parse_life_expectancy(description)
            breed_attributes[term] = description

    return breed_attributes


def parse_height(text, breed_name=None):
    text = text.replace(' inches', '').replace('Minimum: ', '')
    text_split_comma = text.split(', ')
    text_split_semicolon = text.split('; ')

    try:
        # 1, 2, 3 pattern
        if 'up to ' in text:
            description = [0, float(text.replace('up to ', ''))]
        elif len(text_split_comma) > 1 and ', ' in text:
            description = {}
            try:
                for t in text_split_comma:
                    paren_start = t.index('(')
                    paren_end = t.index(')')
                    val = t[:paren_start-1]
                    val_split = val.split('-')
                    val_type = t[paren_start+1:paren_end]
                    if len(val_split) > 1:
                        val_array = [float(i) for i in val_split]
                        description[val_type] = val_array
                    elif len(val_split) == 1:
                        val = val_split[0]
                        description[val_type] = float(val)
                    else:
                        description[val_type] = -1
            except:
                return 'Could not find'
        elif len(text_split_semicolon) > 1 and '; ' in text:
            description = {}
            try:
                for t in text_split_semicolon:
                    paren_start = t.index('(')
                    paren_end = t.index(')')
                    val = t[:paren_start-1]
                    val_split = val.split('-')
                    val_type = t[paren_start+1:paren_end]
                    if len(val_split) > 1:
                        val_array = [float(i) for i in val_split]
                        description[val_type] = val_array
                    elif len(val_split) == 1:
                        val = val_split[0]
                        description[val_type] = float(val)
                    else:
                        description[val_type] = -1
            except:
                return 'Could not find'
        # no commas or semicolons in text
        else:
            text_split = text.split('-')

            if len(text_split) == 1:
                description = float(text_split[0])
            else:
                description = [float(i) for i in text_split]
    except:
        return 'Could not find'

    if breed_name is not None:
        print(breed_name)
        print('{} -> {}'.format(text, description))

    return description


def parse_weight(text, breed_name=None):
    text = text.replace(' pounds', '').replace('Minimum: ', '')
    text_split_comma = text.split(', ')
    text_split_semicolon = text.split('; ')

    try:
        if 'proportionate to height' in text.lower():
            return 'Proportionate to height'
        elif 'not exceeding ' in text.lower():
            text = text.replace('not exceeding ', '')
            return [0, float(text)]
        elif 'under ' in text.lower():
            text = text.replace('under ', '')
            return [0, float(text)]
        elif len(text_split_comma) > 1:
            description = {}
            try:
                for t in text_split_comma:
                    paren_start = t.index('(')
                    paren_end = t.index(')')
                    val = t[:paren_start-1]
                    val_split = val.split('-')
                    val_type = t[paren_start+1:paren_end]
                    if len(val_split) > 1:
                        val_array = [float(i) for i in val_split]
                        description[val_type] = val_array
                    elif len(val_split) == 1:
                        val = val_split[0]
                        description[val_type] = float(val)
                    else:
                        description[val_type] = -1
            except:
                return 'Could not find'
        elif len(text_split_semicolon) > 1:
            description = {}
            try:
                for t in text_split_semicolon:
                    paren_start = t.index('(')
                    paren_end = t.index(')')
                    val = t[:paren_start-1]
                    val_split = val.split('-')
                    val_type = t[paren_start+1:paren_end]
                    if len(val_split) > 1:
                        val_array = [float(i) for i in val_split]
                        description[val_type] = val_array
                    elif len(val_split) == 1:
                        val = val_split[0]
                        description[val_type] = float(val)
                    else:
                        description[val_type] = -1
            except:
                return 'Could not find'
        else:
            text_split = text.split('-')
            if len(text_split) == 2:
                description = [float(i) for i in text_split]
            else:
                description = float(text)
    except:
        return 'Could not find'

    if breed_name is not None:
        print(breed_name)
        print('{} -> {}'.format(text, description))

    return description


def parse_life_expectancy(text, breed_name=None):
    text = text.replace(' years', '')
    if '-' in text:
        life_expectancy = text.split('-')
    elif '–' in text:
        life_expectancy = text.split('–')
    else:
        life_expectancy = []

    if type(life_expectancy) == list and len(life_expectancy) == 2:
        if len(life_expectancy) == 2 and '+' in life_expectancy[1]:
            life_expectancy = [life_expectancy[0], 20]
    elif '+' in text:
        life_expectancy = text.replace('+', '')
        life_expectancy = [life_expectancy, 20]
    elif '~' in text:
        approx = int(text.replace('~', ''))
        life_expectancy = [approx-1, approx+1]
    elif text.lower() == 'late teens':
        life_expectancy = [17, 20]
    else:
        try:
            approx = int(text)
            life_expectancy = [approx-1, approx+1]
        except:
            life_expectancy = [-1]

    if breed_name is not None:
        print(breed_name)
        print('{} -> {}'.format(text, life_expectancy))

    life_expectancy = [int(i) for i in life_expectancy]
    return life_expectancy


def extract_traits(html_text):
    breed_traits = {}
    breed_tabs = html_text.find_all(
        'div', 'tabs__panel-wrap')[1].find_all('div', {'class': 'tabs__tab-panel'})
    for tab in breed_tabs:
        tab_sections = tab.find_all('div', {'class': 'graph-section__inner'})
        for section in tab_sections:
            title = section.find(
                'h4', {'class': 'bar-graph__title'})
            description = section.find(
                'div', {'class': 'bar-graph__text'})
            percentage = section.find('div', {'class': 'bar-graph__section'})
            if title is not None:
                title = title.text
                breed_traits[title] = {}
            else:
                raise Exception('Cannot find title for a title.')
            if description is not None:
                description = description.text
                breed_traits[title]['description'] = description
            else:
                raise Exception('Cannot find description for a description.')
            if percentage is not None:
                percentage = percentage['style']
                percentage = percentage.split(';')
                for p in percentage:
                    if 'width:' in p:
                        percentage = p[-4:].replace('%',
                                                    '').replace('px', '').strip()
                        percentage = int(percentage)
                breed_traits[title]['percentage'] = percentage

    return breed_traits


if __name__ == '__main__':
    main()
