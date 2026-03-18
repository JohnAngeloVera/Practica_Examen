# Titulo del Mardown

## Subtitulo/Indice

1. [Cosas Randoms](#1-cosas-randoms)
2. [Tablas](#2-tablas)
3. [El Resto](#3-el-resto)



## 1. Cosas Randoms

Esto es un parrafo normal

Esto es otra linea 

---

sirve para poner una linea entre medias o separatoria

<br>

para dejar mas hueco el mitico <br>

**Para que se vea en negrita seria el doble asterisco**

*Para que sea italica se poner unicamente uno*

***Se puede jugar con*:AMBAS**

:+1: :exclamation: :grey_question:

:-1:

[Enlace](https://www.google.com/?hl=es&zx=1773810919697&no_sw_cr=1)

- listas que se pueden anidar hasta en 3
    - segunda lista
        - tercera lista

---

- [ ] no hecho

- [X] hecho

<br><br><br><br>

---

## 2. Tablas

|   Cosas Importantes |    Cosas Importantes | 
|-------------------- | ---------------------|
|   Los amigos        |   Los amigos        |
|   La familia        |   La familia        |
|   Los objetivos     |   Los objetivos     |
|   Ser buena gente   |   Ser buena gente   |


<table>
    <thead>
        <tr>
            <th>Real Madrid</th>
            <th>Real Madrid</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>34-454</td>
            <td>fefefe</td>
        </tr>
        <tr>
            <td>34-454</td>
            <td>fefefe</td>
        </tr>
        <tr>
            <td>34-454</td>
            <td>fefefe</td>
        </tr>
        <tr>
            <td>34-454</td>
            <td>fefefe</td>
        </tr>
    </tbody>
</table>


## 3. El Resto

NOS QUEDARIA principalmente como se documenta el codigo 

si queremos una linea o escribir antes de esa linea `Comilla francesa`


si queremos el bloque completo seria

```(lenguaje)
String nombre = "Juan";
```

Es importante poner bien el lenguaje del codigo para que se vea adecuadamente

```python
def operation_numbers(num1: int, num2: int) -> None:

    add_nums = num1 + num2
    sub_nums = num1 - num2
    mul_nums = num1 * num2
    div_nums = num1 / num2 if num2 != 0 else 0
    print(f"{add_nums}\n{sub_nums}\n{mul_nums}\n{div_nums}")
```

<pre>
    <code>
    def operation_numbers(num1: int, num2: int) -> None:

    add_nums = num1 + num2
    sub_nums = num1 - num2
    mul_nums = num1 * num2
    div_nums = num1 / num2 if num2 != 0 else 0
    print(f"{add_nums}\n{sub_nums}\n{mul_nums}\n{div_nums}")



    </code>
</pre>