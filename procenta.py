def vypocitat_procento(pocet_bodu,celkovy_pocet_bodu):
    if celkovy_pocet_bodu == 0:
        return "Chyba: celkový počet bodů nemůže být nulový"
    procento = (pocet_bodu / celkovy_pocet_bodu) * 100
    return procento

def main():
    try:
        pocet_bodu = float(input("Zadejte počet získaných bodů: "))
        celkovy_pocet_bodu = float(input("Zadejte celkový počet bodů:"))

        procento = vypocitat_procento(pocet_bodu,celkovy_pocet_bodu)

        if isinstance(procento, str):
            print(procento)
        else:
            print(f"Získali jste {procento:.2f}% z  celkového počtu bodů.")

    except ValueError:
        print("Chyba: Prosím zadejte platné číslo.")

if __name__ == "__main__":
    main()