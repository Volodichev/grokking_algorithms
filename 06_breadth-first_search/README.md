# Глава 6. Поиск в ширину (Breadth-First Search)

## Что такое граф?

Графы используются для моделирования связей между объектами. Они состоят из *узлов* и *ребер*. Связанные ребрами узлы называются *соседями*.

Графы бывают направленными (отношения действуют только в одну сторону) и ненаправленными.

Направленный граф, у которого нет ребер, идущих в обратном направлении, называется *деревом*.

## Поиск в ширину

Алгоритм поиска в графе. Помогает ответить на вопросы двух типов:

* Тип 1: существует ли путь от узла А к узлу В?
* Тип 2: как выглядит кратчайший путь от узла А к узлу В (путь с минимальным количеством сегментов)?

Поиск в ширину начинается от связей первого уровня, затем переходит к связям второго уровня и т.дю - распространяется *в ширину*.

### Очередь

Для проверки узлов используется специальная структура - очередь (первым вошел, первым вышел).

Связи первого уровня первыми попадают в очередь проверки. Затем в нее добавляются связи второго и далее уровней.

Таким образом, всегда сначала будут проверены ближние узлы - и будет найден самый короткий путь до целевого узла.

### Реализация графа

Для программной реализации графов используются хеш-таблицы. В качестве ключа используется узел графа, а значением является массив соседних с ним узлов.

### Пример

Ищем продавца манго среди друзей на Facebook.

Сначала добавляем в очередь всех своих друзей (связи первого уровня). Проверяем их.

Если человек не является продавцом манго, выбрасываем его из очереди и добавляем в него всех его друзей (связи второго уровня). И так далее, пока очередь не опустеет или не будет найден продавец манго.

Важно отмечать уже проверенные связи, так как иначе может возникнуть бесконечный цикл проверки, или некоторые узлы будут проверяться несколько раз.

***

### Время выполнения

Проход по всем ребрам графа - O(количество_ребер)

Добавление всех узлов в очередь - O(количество_узлов)

Таким образом, время выполнения алгоритма Поиска в ширину составляет O(V + E),
где V - количество вершин, а E - количество ребер графа.

## Топологическая сортировка

Способ построения упорядоченного списка на основе графа.

Если узел А зависит от узла В, то узел А находится в более поздней по­зиции списка.

При этом несвязанные линии узлов могут пересекаться внутри списка, но порядок в них все равно сохраняется.