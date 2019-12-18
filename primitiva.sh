#!/bin/bash

#Número de combinciones deseadas
i=4

until [ $i -lt 0 ]
do
    python primitiva.py
    ((i--))
done

