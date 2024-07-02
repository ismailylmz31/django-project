from django.shortcuts import render


kategori_liste = ["macera", "bilim-kurgu", "komedi"]
film_liste = [
    {
        "id": 1,
        "film_adi": "IRON MAN",
        "film_aciklamasİ": "IRON MAN BASLIYOR",
        "resim": "1.png",
        "anasayfa": True
    },
    {
        "id": 2,
        "film_adi": "IRON MAN2",
        "film_aciklamasİ": "IRON MAN YENİ ZIRHLAR",
        "resim": "2.jpg",
        "anasayfa": False
    },
    {
        "id": 3,
        "film_adi": "IRON MAN3",
        "film_aciklamasİ": "IRON MAN YENİ HOBİ",
        "resim": "3.jpg",
        "anasayfa": False

    },
    {
        "id": 4,
        "film_adi": "IRON MAN4",
        "film_aciklamasİ": "KALBİMİZDE YAŞIYOR İ LOVE U 3000",
        "resim": "4.jpg",
        "anasayfa": False
    }
]
# Create your views here.
def home(request):
    data = {
        "kategoriler": kategori_liste,
        "filmler": film_liste
    }
    return render(request, "index.html", data)


def movies(request):
    data = {
        "kategoriler": kategori_liste,
        "filmler": film_liste
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data = {
        
        "id": id
    }
    return render(request, "details.html", data)
