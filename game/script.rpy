define p = Character('peashooter', color="#c8ffc8")
define s = Character('sunflower', color="#c8c8ff")
define z = Character('zombies', color="#c8c8ff")
define n = Character('narator', color="#c8c8ff")

define audio.sunflower1 = "Voicy_Piano music sound effect.mp3"
define audio.sunflower2 = "Voicy_Plants vs Zombies theme music.mp3"
define audio.sunflower3 = "Voicy_Zombie roaring sound effect.mp3"


image bg rumput = "bg/latar1.png"
image bg rumput malam = "bg/latar2.png"
image peashooter = im.Scale("char/peashooter.png",500,600)
image zombies = im.Scale("char/zombies.png",400,600)
image sunflower = im.Scale("char/sunflower.png",400,600)
image sunflower2 = im.Scale("char/sunflower2.png",400,600)
image sun =  im.Scale("char/sun.png",200,200)
image sun2 =  im.Scale("char/sun2.png",200,200)
image sun3 =  im.Scale("char/sun3.png",200,200)
image sevenam =  im.Scale("char/7am.png",300,300)
image lonceng =  im.Scale("char/lonceng.png",300,300)
image kacang =  im.Scale("char/kacang.png",200,200)
image zombies_dead = im.Scale("char/zombies_dead.png",400,600)

transform left1:
    xalign 0
    yalign 0.9
transform left2:
    xalign 0.3
    yalign 1
transform right1:
    xalign 0.9
    yalign 0.9
transform right2:
    xalign 0.7
    yalign 1
transform right3:
    xalign 1
    yalign 1
transform center:
    xalign 0.5
    yalign 0.5
transform center2:
    xalign 0.9
    yalign 0.5
transform flip:
    xzoom-1

init python:
    def drag_placed(drags, drop):
        if not drop:
            return
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True

screen dragA():
    fixed:
        draggroup:
            drag:
                drag_name "kacang1"
                xpos 0.2
                ypos 0.5
                draggable True
                droppable False
                drag_raise True
                dragged drag_placed
                add "kacang"

            drag:
                drag_name "kacang2"
                xpos 0.35
                ypos 0.5
                draggable True
                droppable False
                drag_raise True
                dragged drag_placed
                add "kacang"
            drag:
                drag_name "zombies_dead"
                xpos 0.35
                ypos 0.5
                draggable True
                droppable False
                drag_raise True
                dragged drag_placed
                add "zombies_dead"
            drag:
                drag_name "sunflower2"
                xpos 0.5
                ypos 0.5
                draggable True
                droppable False
                drag_raise True
                dragged drag_placed
                add "sunflower2"




label start:

    scene bg rumput with fade
    play sound sunflower1
    n "Di suatu pagi yang cerah peashooter dan sunflower sedang berjemur di depan rumahnya agar tubuhnya mendapatkan asupan matahari yang banyak untuk proses fotosintesis"

    n "Fotosintesis itu bagi peashooter menghasilkan kacang-kacang yang bisa ditembakkan untuk menghadang para zombie"

    n "Sementara bagi sun flower, fotosintesis dapat menghasilkan matahari matahari baru untuk memperkuat energi"

    show peashooter at left1 with dissolve
     
    p "Hai sun flower, semakin hari matahari yang kamu hasilkan semakin banyak yaa"

    
    show sunflower at right1 with dissolve
    show sun at right2 with dissolve
    show sun2 at right3 with dissolve
    s "Hai peashooter, betul sekali aku ingin memperkuat energiku dengan cepat. Aku tidak menginginkan bangunan ini hancur hanya karna kita lalai dalam menghadang zombies"

    p "Kita sama-sama tumbuhan, aku ingin mengetahui apa hal yang kamu lakukan agar matahari bisa semakin banyak dalam waktu yang cepat? Aku ingin coba terapkan hal itu agar kacang ku semakin cepat bertambah jugaa"

    show sevenam at center with dissolve
    s "Oh, untuk itu aku selalu melakukan hal sederhana saja. Setiap pukul 7 pagi aku selalu berjemur dengan rutin tanpa bolong sekalipun"

    hide sevenam
    p "Apakah ada lagi?"

    s "Aku juga ketika akan tumbuh selalu memilih tempat yang kaya akan unsur hara"

    p "Oh, seperti itu ternyataa. Baik akan kulakukan"

    hide sunflower
    hide sun
    hide sun2
    hide peashooter

    scene bg rumput malam with fade
    play sound sunflower2
    n "Hari mulai malam, matahari pun semakin tenggelam. Dimalam itu peashooter sudah berjanji akan bangun pagi dan rutin untuk berjemur"
    scene bg rumput with fade

    show sunflower at right1 with dissolve
    show sun at right2 with dissolve
    show sun2 at right3 with dissolve

    play sound sunflower1
    n "Matahari mulai terbit, peashooter segera bangun untuk berjemur. Tidak disangka ternyata sudah ada sunflower disana. Betul dia tidak berbohong"
    
    show peashooter at left1 with dissolve
    p "Wah ternyata benar aktivitas yang kamu lakukan rutin seperti ini ya"

    s "Betul"
    
   
    show lonceng at center with dissolve
    play music sunflower2
    n "Ketika mereka sedang asyik berjemur, tiba-tiba lonceng rumah berbunyi keras, itu menandakan area rumah sedang berbahaya"

    n "Ternyata Zombies mulai datang. Dengan langkah gontainya dia terus berjalan menuju ke arah kita. Dia akan segera menghancurkan bangunan kita"

    hide lonceng
    show sunflower at center with dissolve
    show peashooter at left1 with dissolve
    p "Bagaimana ini, kita harus bertindak seperti apaa?"

    s "Kamu gunakan dulu alat penembak kacang mu untuk menghadang Zombies, sedang akan aku disini akan coba untuk mengumpulkan  matahari supaya kita bisa menambah personil tanaman lagi"

    show sun3 at center2 with dissolve

    p "Oke akan kulakukan. Kita bekerja sama yaaa"


    show zombies at right1 with dissolve
    play music sunflower3

    z "Hahahahah aku datang. Aku akan hancurkan rumah jelekmu itu"

    

    
    

    p "kami tidak takut kami punya segala cara untuk menghadang mu, rasakan kacang yang aku tembakkan ini"

    s "Ayo tembakkan terus, disini hari sedang cerah aku akan terus memproduksi matahari agar bisa segera aku tukar dengan tanaman lainnya"

    z "Aku mendekat, sedekat dekatnya. Aku bawa rombongan zombies lainnya"
    
    call screen dragA
    s "wah tanaman baru sudah muncul, ayo letakkan di tanah yang kaya akan nutrisi, pilih masing masing 1 peashooter dan sunflower lagi"

    z " Awass!! kita semakin siap menghancurkan rumah itu"

    n "Peashooter terus menembakkan berulang ulang kacangnya. Ajaib sekali sekarang zombies mulai semakin gontai, akhirnya satu persatu mati. Namun zombies lain berdatangan kembali"

    z "aaaa aku matii, dorr"

    hide zombies
    show zombies_dead at right1 with dissolve
  
    
    

    p "Kerjasama yang bagus sun flower, kita kuatkan lagi pertahanan kita untuk melawan zombies lainnya"


    