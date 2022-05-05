# solar-system
 Simulateur de Système Solaire


```mermaid
flowchart TD
    A[def main] -- transmission des entrées utilisateur --> B[class ecran];
    A -- transmission de la date --> C[class Gestion_Planete];
    C -- demande les calculs au système de physique --> D(class Planete);
```
