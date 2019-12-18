#!/bin/bash

#Número de combinaciones a generar
i=4

until [ $i -lt 0 ]
do
    python euromillones.py
    ((i--))
done

