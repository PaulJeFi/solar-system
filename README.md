# solar-system
 Simulateur de Système Solaire


```mermaid
flowchart TD
    AP{APPLICATION};
    A[def main] -- transmission des entrées utilisateur --> B[class ecran];
    A -- transmission de la date --> C[class Gestion_Planete];
    C -- demande les calculs au système de physique --> D(class Planete);
    B -- demande quoi afficher à --> E[ ];
    E -- signes astologiques --> F(def astro_fra);
    E -- signes astologiques chinois --> G(def astro_chn);
    E -- niveau de zoom --> H(def zoom_slider);
    A -- affichage de l'arrière plan --> I(class Trainee);
    J(def update_time) -- actualise le temps --> A;
    A -- appelle à chaque frame --> J;
    A -- demande à chaque frame --> K(def vitesse_lecture);
    K -- indique la vitesse de lecture --> A;
    
    AP -- Entrées utilisateur --> A;
    I -- affichage --> AP;
    C -- affichage --> AP;
    B -- affichage --> AP;
```
