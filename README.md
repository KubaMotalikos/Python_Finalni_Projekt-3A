# Střelnice

Střelnice je arkádová střílečka v programovacím jazyce Ptyhon za použití knihovny Pygame.

## Funkce

- **Různé úrovně:** Hra obsahuje tři úrovně, každá s unikátními cíly a pozadím.
- **Režimy hry:** Hráči mohou hrát v různých režimech, jako je tréninkový režim, režim s omezenými náboji, režim s časovým limitem a režim na nejlepší čas.
- **Pauza a Game Over:** Hra umožňuje pauzování a zobrazení obrazovky konce hry s výsledným skóre.

## Instalace

1. Ujistěte se, že máte nainstalovaný Python a Pygame. Můžete je nainstalovat pomocí následujícího příkazu:
    ```bash
    pip install pygame
    ```

2. Stáhněte si nebo naklonujte tento repozitář.

3. Ujistěte se, že máte v adresáři soubory fontů a obrázků:
    - `myFont.ttf`
    - `mainmenu.png`
    - `gameover.png`
    - `pause.png`
    - Obrázky cílů: `obr1.png`, `obr2.png`, `obr3.png`
    - Obrázky pozadí: `pozadi1.png`, `pozadi2.png`, `pozadi3.png`
    - Obrázky zbraní: `gun1.png`, `gun2.png`, `gun3.png`
    - Obrázek banneru: `banner.png`

## Použití

1. Spusťte hlavní soubor hry:
    ```bash
    python main.py
    ```

2. V hlavním menu si vyberte herní režim kliknutím na příslušné tlačítko.

3. Střílejte na cíle pohybem myši a kliknutím levého tlačítka myši.

4. Hru můžete pozastavit nebo ukončit pomocí tlačítek v pravém dolním rohu.

## Herní Režimy

- **Tréninkový režim:** Hráč má neomezené náboje a čas.
- **Režim s omezenými náboji:** Hráč má omezený počet nábojů.
- **Režim s časovým limitem:** Hráč má omezený čas na dosažení co nejvyššího skóre.
- **Režim na nejlepší čas:** Hráč se snaží dosáhnout nejlepšího času na dokončení všech úrovní.

## Přispěvky

Pokud byste chtěli přispět do tohoto projektu, neváhejte vytvořit pull request.
