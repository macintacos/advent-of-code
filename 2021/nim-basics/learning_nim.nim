import terminaltables
import math
import std/algorithm
import std/strformat
import std/sequtils
import strutils

echo "Exercise 1"
proc collatzConjecture(input: int): int =
    echo input
    if input == 1: return 1 # Break early

    var new_input: int
    if input mod 2 == 1: # odd
        new_input = input * 3 + 1
    else:
        new_input = input div 2

    return collatzConjecture(new_input)

discard collatzConjecture(8)
discard 8.collatzConjecture

echo "Exercise 2"
let name = "Supercalafragalisticexpialadocious"

for letter in name:
    if contains($letter, {'a', 'e', 'i', 'o', 'u', 'y'}):
        echo letter

echo "Exercise 4" # exercise 3 is dumb
type ConvertTypes = enum
    cm, inch

proc convert(inputVals: seq[float], fromType: ConvertTypes,
        toType: ConvertTypes) =
    # Default conversion factor
    var conversionFactor: float = 1.0

    #[
        Figure out what kind of conversion we're doing.
        Currently, only supports inch <-> cm
    ]#
    case fromType:
        of cm:
            case toType:
                of inch:
                    conversionFactor = 1.0 / 2.54
                else: discard
        of inch:
            case toType:
                of cm:
                    conversionFactor = 2.54
                else: discard

    # Do the actual conversions to get new sequence of values
    let newVals: seq[float] = block:
        var v: seq[float]
        for val in inputVals: v.add(val * conversionFactor)
        v

    # Build the table
    let conversionTable = newUnicodeTable()
    conversionTable.separateRows = false
    conversionTable.setHeaders(@[$fromType, $toType])

    for idx, convertedVal in newVals:
        conversionTable.addRow(@[$inputVals[idx], $convertedVal])

    printTable(conversionTable)

var starterVals = @[1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0]
convert(starterVals, ConvertTypes.cm, ConvertTypes.inch)
convert(starterVals, ConvertTypes.inch, ConvertTypes.cm)

echo "Exercises for containers"
echo "Exercise 1"

# This syntax feels like cheating?
var someArray: array[10, int] = block:
    var v: array[10, int]
    for num in 1..10: v[num - 1] = num * 10
    v

for idx, elem in someArray:
    if idx mod 2 == 1: # odd
        echo elem
    else: # even
        someArray[idx] = elem * 5

echo someArray

echo "Exercise 2 & 3"

proc collatzConjectureRedux(input: seq[int]): seq[int] =
    var
        tmpInput: seq[int]
        latestVal = input[^1]

    if latestVal == 1: return input # Break early

    var newInput: int
    if latestVal mod 2 == 1: # odd
        newInput = latestVal * 3 + 1
    else:
        newInput = latestVal div 2

    shallowCopy tmpInput, input
    tmpInput.add(newInput)

    return collatzConjectureRedux(tmpInput)

echo collatzConjectureRedux(@[670617279])
echo collatzConjectureRedux(@[670617279]).len

var
    collatzPairs: seq[tuple[startingNumber: int, length: int]] = @[]
    collatzLengths: seq[int] = @[]

for num in 2..1000:
    let collatzLength = collatzConjectureRedux(@[num]).len
    collatzLengths.add(collatzLength)
    collatzPairs.add((startingNumber: num, length: collatzLength))

let
    indexOfMax = collatzLengths.maxIndex
    collatzMax = collatzPairs[indexOfMax]
echo fmt"The highest length is from starting number '{collatzMax.startingNumber}', which has a length of '{collatzMax.length}'"

proc plus(x, y: int): int =
    return x+y

proc multiply(x, y: int): int =
    return x*y

let
    a = 2
    b = 3
    c = 4

# This syntax breaks my brain
echo a.plus(b) == plus(a, b)
echo c.multiply(a) == multiply(c, a)
echo a.plus(b).multiply(c)
echo c.multiply(b).plus(a)

proc findBiggest(a: seq[int]): int =
    for number in a:
        if number > result:
            result = number

# let g = @[3, -5, 11, 33, 7, -15]
# echo findBiggest(g)

proc keepOdds(a: seq[int]): seq[int] =
    for number in a:
        if number mod 2 == 1:
            result.add(number)

let f = @[1, 6, 4, 43, 57, 34, 98]
echo f.keepOdds()

proc isDivisibleBy3(x: int): bool =
    return x mod 3 == 0

proc filterMultiplesOf3(a: seq[int]): seq[int] =
    for i in a:
        if i.isDivisibleBy3:
            result.add(i)

let
    g = @[2, 6, 5, 7, 9, 0, 5, 3]
    h = @[5, 4, 3, 2, 1]
    i = @[626, 45390, 3219, 4210, 4126]

echo g.filterMultiplesOf3
echo h.filterMultiplesOf3
echo filterMultiplesOf3 i

proc greet(name: string): void =
    echo fmt"Yo, {name}"

let names = @["Julian", "Someone", "Else"]
for name in names: name.greet

proc findMax3(vals: seq[int]): int =
    if vals.len != 3:
        echo "Must provide 3 values in a sequence"
        return 0

    var tmpVals: seq[int] = vals
    tmpVals.sort()

    let maxVal = tmpVals[^1]

    return maxVal

var threeNums = @[1, 4, 3]
echo threeNums.findMax3

type Point = object
    x: float
    y: float

proc sumPoints(point1, point2: Point): Point =
    var newPoint: Point

    newPoint.x = point1.x + point2.x
    newPoint.y = point1.y + point2.y

    return newPoint

var
    pointA = Point(x: 1.0, y: 2.0)
    pointB = Point(x: 1.0, y: 2.0)
    pointAB = sumPoints(pointA, pointB)

echo pointAB

var
    tickCounter = 0
    tockCounter = 0

proc tick()
proc tock()

proc tick() =
    echo "tick"
    tickCounter += 1
    tock()

proc tock() =
    echo "tock"
    if tickCounter >= 20: return
    tockCounter += 1
    tick()

tick()

let
    someString = "My string with whitespace"
    exclamation = "!"

echo someString.split()
echo someString.toUpperAscii()
echo exclamation.repeat(5)

let
    degrees = 30.0
    cRadians = degrees.degToRad

echo cRadians
echo sin(cRadians).round(2)
echo 2^5

type
    Direction = enum
        north, east, south, west
    BlinkLights = enum
        off, on, slowBlink, mediumBlink, fastBlink
    LevelSetting = array[north..west, BlinkLights]

var
    level: LevelSetting

echo level
level[north] = on
level[south] = slowBlink
level[east] = fastBlink
echo level
echo low(level)
echo len(level)
echo high(level)
echo level[west]

type LightTower = array[1..10, LevelSetting]
var tower: LightTower

tower[1][north] = slowBlink
tower[1][east] = mediumBlink
echo len(tower)
echo len(tower[1])
echo tower

type
    IntArray = array[0..5, int]
    QuickArray = array[6, int]

var
    x: IntArray
    y: QuickArray

x = [1, 2, 3, 4, 5, 6]
y = x
for i in low(x) .. high(x):
    echo x[i], y[i]


var
    fruits: seq[string]
    capitals: array[3, string]

capitals = ["New York", "London", "Berlin"]
fruits.add("Banana")
fruits.add("Mango")

proc openArraySize(oa: openArray[string]): int =
    oa.len

echo openArraySize(fruits)
echo openArraySize(capitals)

proc myWriteln(f: File, a: varargs[string, `$`]) =
    for s in items(a):
        write(f, s)
    write(f, "\n")

myWriteln(stdout, "abc", "abc", "xyz")
myWriteln(stdout, ["abc", "abc", "xyz"])
myWriteln(stdout, 123, "abc", 4.0)

var
    first = "Nim is a programming language"
    second = "Slices are useless"

echo first[7..12]
second[11..^1] = "useful"
echo second

type Person* = object
    name*: string
    age: int

var person1 = Person(name: "Peter", age: 30)
echo person1.name
echo person1.age

var person2 = person1
person2.age += 14
echo person1.age
echo person2.age


type
    PersonTuple = tuple
        name: string
        age: int
    PersonX = tuple[name: string, age: int]
    PersonY = (string, int)

var
    person: PersonTuple
    personX: PersonX
    personY: PersonY

person = (name: "Peter", age: 30)
personX = person

personY = ("Peter", 30)
person = personY
personY = person

echo person.name
echo person.age
echo person[0]
echo person[1]

var building: tuple[street: string, number: int]
building = ("Rue del Percebe", 13)
echo building.street

import std/os

let
    path = "usr/local/nimc.html"
    (dir, fname, ext) = splitFile(path)
    baddir, badname, badext = splitFile(path)

echo dir, fname, ext
echo baddir
echo badname
echo badext
