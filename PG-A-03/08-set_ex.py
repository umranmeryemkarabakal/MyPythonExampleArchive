"""color = input("bir renk giriniz")

match color:
    case "yellow":
        print("yellow")
    case "blue":
        print("blue")
    case otherColor:
        print(f"{otherColor}")"""
        
color = {"mavi","siyah","pembe"}

match color:
    case ("sarı"):
        print("seçtiğiniz renk sarıdır")
    case ("mavi","siyah") | ("siyah","mor"):
        print("seçtiğiniz renk mavi veya siyahtır")
    case ("mavi", *otherColor):
        print(f"seçtiğiniz renk {otherColor}")
    case (_,"siyah","pembe"):
        print("seçtiğiniz renk siyah veya pembe")

