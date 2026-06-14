from django.shortcuts import render, redirect
from .models import Campaign, DonationCenter, PreparednessCheck
from .forms import VolunteerForm
from django.contrib.auth.decorators import login_required
from .models import PreparednessCheck
from .forms import PreparednessCheckForm
from .forms import DonationForm
from .forms import DonationForm
def donation_home(request):
    campaigns = Campaign.objects.filter(active=True).order_by("-created_at")
    centers = DonationCenter.objects.filter(active=True)

    return render(
        request,
        "donation_home.html",
        {
            "campaigns": campaigns,
            "centers": centers,
        }
    )


def information(request):
    return render(request, "information.html")


def volunteer(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("volunteer_success")
    else:
        form = VolunteerForm()

    return render(
        request,
        "volunteer.html",
        {
            "form": form,
        },
    )


AFETLER = {
    "deprem": {
        "title": "Deprem",

        "description": """
Deprem, yer kabuğunu oluşturan levhaların hareket etmesi sonucunda yer altında
biriken enerjinin ani şekilde açığa çıkmasıyla meydana gelen doğal bir afettir.
Bu enerji sismik dalgalar halinde yayılır ve yeryüzünde sarsıntı oluşturur.

Türkiye, aktif fay hatları üzerinde bulunan bir ülke olduğu için deprem riski
yüksek bölgelerden biridir. Bu nedenle deprem bilinci, yapı güvenliği ve doğru
davranış biçimleri hayati önem taşır.
""",

        "extra_sections": [
            {
                "heading": "Deprem Nasıl Oluşur?",
                "text": """
Yer kabuğu büyük levhalardan oluşur. Bu levhalar sürekli hareket halindedir.
Levhaların hareketi sırasında fay hatlarında enerji birikir. Kayaçların dayanma
sınırı aşıldığında kırılma meydana gelir ve deprem oluşur.

Depremler önceden kesin olarak tahmin edilemez. Bu nedenle en etkili korunma
yolu hazırlıklı olmak, güvenli yapılar inşa etmek ve afet planı oluşturmaktır.
"""
            },
            {
                "heading": "Deprem Öncesi Hazırlık",
                "text": """
Deprem olmadan önce yapılacak hazırlıklar can güvenliği açısından çok önemlidir.
Evde devrilebilecek dolap, kitaplık ve beyaz eşyalar duvara sabitlenmelidir.
Yatakların üzerine ağır tablo veya raf asılmamalıdır.

Aile bireyleriyle bir afet planı hazırlanmalı, ev dışında buluşulacak güvenli
bir toplanma noktası belirlenmelidir. Her evde kolay ulaşılabilecek bir acil
durum çantası bulundurulmalıdır.
"""
            },
            {
                "heading": "Deprem Anında Doğru Davranış",
                "text": """
Deprem sırasında panik yapmak tehlikeyi artırabilir. Bina içindeyseniz pencere,
cam, dolap ve devrilebilecek eşyalardan uzak durmalısınız. Güvenli bir noktada
Çök-Kapan-Tutun hareketini uygulamak en doğru davranışlardan biridir.

Asansör kesinlikle kullanılmamalıdır. Merdivenlere koşmak veya balkondan atlamak
ciddi yaralanmalara neden olabilir.
"""
            },
            {
                "heading": "Deprem Sonrası",
                "text": """
Sarsıntı bittikten sonra bina kontrollü şekilde terk edilmeli ve belirlenen
toplanma alanına gidilmelidir. Hasarlı binalara tekrar girilmemelidir çünkü
artçı depremler yeni yıkımlara neden olabilir.

Gaz kokusu alınırsa elektrik düğmelerine dokunulmamalı, ateş yakılmamalı ve
yetkililere haber verilmelidir. Resmi kurumların açıklamaları takip edilmeli,
doğrulanmamış bilgiler paylaşılmamalıdır.
"""
            },
            {
                "heading": "Psikolojik Etkiler",
                "text": """
Deprem sonrasında korku, kaygı, uykusuzluk ve stres yaşanması normaldir.
Özellikle çocuklar, yaşlılar ve engelli bireyler daha fazla desteğe ihtiyaç
duyabilir.

Uzun süre devam eden yoğun kaygı, panik, uyku bozukluğu veya travma belirtileri
varsa profesyonel psikolojik destek alınmalıdır.
"""
            },
        ],

        "before": [
            "Acil durum çantası hazırlayın.",
            "Dolap ve rafları duvara sabitleyin.",
            "Aile afet planı oluşturun.",
            "Toplanma alanınızı öğrenin.",
            "Gaz vanası ve elektrik şalterinin yerini öğrenin.",
        ],

        "during": [
            "Çök-Kapan-Tutun hareketini uygulayın.",
            "Pencerelerden ve camlardan uzak durun.",
            "Asansör kullanmayın.",
            "Panik yapmamaya çalışın.",
            "Başınızı ve boynunuzu koruyun.",
        ],

        "after": [
            "Hasarlı binalara girmeyin.",
            "Gaz kaçağı ihtimaline karşı dikkatli olun.",
            "Artçı depremlere karşı hazırlıklı olun.",
            "112 ve AFAD duyurularını takip edin.",
            "Toplanma alanına gidin.",
        ],

        "dont": [
            "Asansör kullanmayın.",
            "Balkondan veya pencereden atlamayın.",
            "Telefonu gereksiz yere meşgul etmeyin.",
            "Hasarlı binaya geri girmeyin.",
        ],

        "faq": [
            (
                "Deprem sırasında kapı eşiğinde durmalı mıyım?",
                "Hayır. Güncel afet rehberlerinde güvenli bir eşyanın yanında Çök-Kapan-Tutun hareketi önerilmektedir."
            ),
            (
                "Depremden sonra eve tekrar girebilir miyim?",
                "Bina hasarlıysa veya yetkililer güvenli olduğunu belirtmediyse girilmemelidir."
            ),
        ],
    },

    "yangin": {
        "title": "Yangın",

        "description": """
Yangın, kontrol dışına çıkan ateşin can ve mal güvenliğini tehdit edecek şekilde
yayılmasıdır. Ev, iş yeri, araç ve orman yangınları farklı nedenlerle ortaya
çıkabilir.

Yangınların önemli bir bölümü ihmal, elektrik arızası, dikkatsiz kullanım veya
yanıcı maddelerin hatalı depolanması nedeniyle oluşur.
""",

        "extra_sections": [
            {
                "heading": "Yangın Nasıl Başlar?",
                "text": """
Yangının oluşması için ısı, oksijen ve yanıcı madde gerekir. Bu üç unsur bir
araya geldiğinde yangın başlayabilir. Elektrik kontağı, açık alev, sigara
izmariti, aşırı ısınan cihazlar ve mutfak kazaları en yaygın nedenlerdendir.
"""
            },
            {
                "heading": "Yangın Anında Tahliye",
                "text": """
Yangın sırasında öncelik can güvenliğidir. Duman yoğunluğu varsa yere yakın
ilerlenmelidir çünkü temiz hava zemine daha yakındır. Kapılar açılmadan önce
ısısı kontrol edilmeli, sıcak kapılar açılmamalıdır.

Asansör kullanılmamalı, merdivenlerden güvenli şekilde çıkılmalıdır.
"""
            },
        ],

        "before": [
            "Elektrik tesisatını düzenli kontrol ettirin.",
            "Yangın söndürücü bulundurun.",
            "Ocak ve fırınları gözetimsiz bırakmayın.",
            "Sigara izmaritlerini tamamen söndürün.",
            "Kaçış planı hazırlayın.",
        ],

        "during": [
            "112 Acil Çağrı Merkezi'ni arayın.",
            "Asansör kullanmayın.",
            "Duman varsa eğilerek ilerleyin.",
            "Kapıları açmadan önce sıcaklığını kontrol edin.",
            "Yangın küçükse uygun söndürücü ile müdahale edin.",
        ],

        "after": [
            "Yetkililer izin vermeden binaya girmeyin.",
            "Elektrik ve gaz tesisatını kontrol ettirin.",
            "Hasar tespiti yaptırın.",
        ],

        "dont": [
            "Panik yapmayın.",
            "Asansöre binmeyin.",
            "Yoğun duman içine girmeyin.",
            "Elektrik yangınına suyla müdahale etmeyin.",
        ],

        "faq": [
            (
                "Yangında neden eğilerek ilerlenir?",
                "Çünkü sıcak duman yükselir, zemine yakın bölgede hava daha solunabilir olabilir."
            ),
        ],
    },

    "sel": {
        "title": "Sel",

        "description": """
Sel; yoğun yağış, dere taşması, altyapı yetersizliği veya baraj taşkınları
sonucunda suyun yerleşim alanlarını kaplamasıyla meydana gelen doğal afettir.
Ani gelişebilir ve kısa sürede büyük zarar verebilir.
""",

        "extra_sections": [
            {
                "heading": "Sel Neden Tehlikelidir?",
                "text": """
Sel suları göründüğünden çok daha güçlü olabilir. Az miktardaki hareketli su
bile insanı dengesiz bırakabilir, araçları sürükleyebilir ve elektrik tehlikesi
oluşturabilir.
"""
            },
        ],

        "before": [
            "Meteoroloji uyarılarını takip edin.",
            "Önemli belgeleri su geçirmez dosyada saklayın.",
            "Tahliye planı hazırlayın.",
            "Bodrum ve zemin katlarda değerli eşya bulundurmayın.",
        ],

        "during": [
            "Yüksek bölgelere çıkın.",
            "Sel suyunda yürümeyin.",
            "Elektrik direklerinden uzak durun.",
            "Araçla suya girmeyin.",
        ],

        "after": [
            "Elektrik tesisatını kontrol ettirin.",
            "Kirli suyla temas etmeyin.",
            "Hasarlı binalara girmeyin.",
            "Resmi uyarıları takip edin.",
        ],

        "dont": [
            "Sel suyunda yüzmeyin.",
            "Elektrikli cihazlara dokunmayın.",
            "Su basmış yollara araçla girmeyin.",
        ],

        "faq": [
            (
                "Sel suyunda araç kullanılır mı?",
                "Hayır. Çok sığ görünen su bile aracı sürükleyebilir."
            ),
        ],
    },

    "ilk-yardim": {
        "title": "İlk Yardım",

        "description": """
İlk yardım; sağlık ekipleri gelene kadar olay yerinde mevcut imkanlarla yapılan
bilinçli ve geçici müdahalelerdir. Amaç hayatı korumak, durumun kötüleşmesini
önlemek ve iyileşmeyi kolaylaştırmaktır.
""",

        "extra_sections": [
            {
                "heading": "İlk Yardımda Temel İlkeler",
                "text": """
İlk yardımda önce olay yerinin güvenliği sağlanmalıdır. Yardım eden kişinin
kendini tehlikeye atmaması gerekir. Ardından yaralının bilinci, solunumu ve
kanaması kontrol edilmelidir.
"""
            },
            {
                "heading": "112 Nasıl Aranmalıdır?",
                "text": """
112 arandığında olay yeri açık ve anlaşılır şekilde tarif edilmelidir. Yaralı
sayısı, olayın türü ve mevcut tehlikeler kısa ve net biçimde aktarılmalıdır.
"""
            },
        ],

        "before": [
            "Temel ilk yardım eğitimi alın.",
            "İlk yardım çantası bulundurun.",
            "112'nin nasıl aranacağını öğrenin.",
        ],

        "during": [
            "Önce kendi güvenliğinizi sağlayın.",
            "Bilinci kontrol edin.",
            "112 Acil Çağrı Merkezi'ni arayın.",
            "Kanamayı durdurmaya çalışın.",
            "Gereksiz hareket ettirmeyin.",
        ],

        "after": [
            "Yaralıyı sağlık ekiplerine teslim edin.",
            "Olay hakkında doğru bilgi verin.",
        ],

        "dont": [
            "Bilinçsiz kişiye su vermeyin.",
            "Kırık şüphesi varsa kişiyi hareket ettirmeyin.",
            "Bilmediğiniz müdahaleleri yapmayın.",
        ],

        "faq": [
            (
                "İlk yardım ile tedavi aynı şey midir?",
                "Hayır. İlk yardım, sağlık ekipleri gelene kadar yapılan geçici ve temel müdahaledir."
            ),
        ],
    },

    "acil-canta": {
        "title": "Acil Durum Çantası",

        "description": """
Acil durum çantası; afet sonrasında ilk saatlerde temel ihtiyaçları
karşılayabilmek amacıyla önceden hazırlanan malzemelerin bulunduğu çantadır.
Her birey ve aile için kolay ulaşılabilir yerde saklanmalıdır.
""",

        "extra_sections": [
            {
                "heading": "Çantada Neler Bulunmalıdır?",
                "text": """
Su, dayanıklı gıda, el feneri, pil, powerbank, ilk yardım seti, düdük, battaniye,
kişisel ilaçlar, kimlik fotokopileri ve hijyen malzemeleri temel ihtiyaçlar
arasında yer alır.
"""
            },
        ],

        "before": [
            "Çantayı kolay ulaşılabilir bir yerde saklayın.",
            "Gıda ve ilaçların son kullanma tarihlerini kontrol edin.",
            "Aile bireylerinin özel ihtiyaçlarına göre düzenleyin.",
        ],

        "during": [
            "Tahliye gerekiyorsa çantanızı yanınıza alın.",
            "Malzemeleri kontrollü şekilde kullanın.",
        ],

        "after": [
            "Eksilen malzemeleri tamamlayın.",
            "Çantayı yeniden hazır hale getirin.",
        ],

        "dont": [
            "Son kullanma tarihi geçmiş ürünleri kullanmayın.",
            "Çantayı ulaşılması zor yerlere koymayın.",
        ],

        "faq": [
            (
                "Çanta kaç kişilik hazırlanmalıdır?",
                "Her aile bireyi için ayrı ya da aile büyüklüğüne uygun hazırlanmalıdır."
            ),
        ],
    },

    "acil-telefonlar": {
        "title": "Acil Telefonlar",

        "description": """
Afet ve acil durumlarda doğru kurumlara hızlı ulaşmak hayat kurtarabilir.
Acil telefon numaralarının bilinmesi ve gereksiz yere meşgul edilmemesi önemlidir.
""",

        "extra_sections": [
            {
                "heading": "Acil Arama Yaparken Nelere Dikkat Edilmelidir?",
                "text": """
Konumunuzu net söyleyin, olayın türünü açıklayın ve yaralı sayısı hakkında
bilgi verin. Operatör telefonu kapatmanızı söylemeden aramayı sonlandırmayın.
"""
            },
        ],

        "before": [
            "Acil numaraları telefonunuza kaydedin.",
            "Çocuklarınıza 112'yi öğretin.",
        ],

        "during": [
            "Gereksiz arama yapmayın.",
            "Kısa ve net bilgi verin.",
            "Konumunuzu açık şekilde tarif edin.",
        ],

        "after": [
            "Yetkililerin yönlendirmelerini takip edin.",
        ],

        "dont": [
            "Asılsız ihbarda bulunmayın.",
            "Acil hatları gereksiz yere meşgul etmeyin.",
        ],

        "faq": [
            (
                "112 hangi durumlarda aranmalıdır?",
                "Hayati tehlike oluşturan tüm acil durumlarda 112 aranmalıdır."
            ),
        ],
    },
}

def volunteer_success(request):
    return render(request, "volunteer_success.html")

def disaster_detail(request, slug):
    disaster = AFETLER.get(slug)

    if disaster is None:
        return render(request, "404.html", status=404)

    return render(
        request,
        "disaster_detail.html",
        {
            "disaster": disaster,
        }
    )

@login_required
def preparedness_check(request):
    check, created = PreparednessCheck.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = PreparednessCheckForm(request.POST, instance=check)

        if form.is_valid():
            form.save()
            return redirect("preparedness_check")
    else:
        form = PreparednessCheckForm(instance=check)

    return render(
        request,
        "preparedness_check.html",
        {
            "form": form,
            "check": check,
            "progress": check.progress_percent(),
        },
    )

def donation_create(request):
    if request.method == "POST":
        form = DonationForm(request.POST)

        if form.is_valid():
            donation = form.save()

            if donation.donation_type == "para":
                donation.campaign.collected_amount += donation.amount
                donation.campaign.save()

            return redirect("donation_success")
    else:
        form = DonationForm()

    return render(
        request,
        "donation_create.html",
        {
            "form": form
        }
    )

def donation_success(request):
    return render(request, "donation_success.html")