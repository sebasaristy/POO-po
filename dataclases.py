from dataclasses import dataclass, field, asdict
from typing import List

"""@dataclass
class Persona:
    nombre: str
    edad: int = field(default=36)

    def retornar_edad_por_2(self) -> int:
        return self.edad * 2
     
persona1 = Persona("Juan")
print(asdict(persona1))


@dataclass
class Puesto:
    nombre: str
    persona: Persona

puesto1 = Puesto("Desarrolador", persona1)
print(asdict(puesto1))

print(persona1.retornar_edad_por_2())


@dataclass
class Grupo:
    personas: List[Persona] = field(default_factory=list)


grupo1 = Grupo()
grupo1.personas.append(persona1)"""
