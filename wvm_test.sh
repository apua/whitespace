if [ $# -lt 1 ]; then
    echo "usage: sh $0 wvm.py"
    exit
fi

py3 $1 STL/factorial.stl STL
py3 $1 STL/factorial.stl STL
py3 $1 STL/fibnancy.stl STL
py3 $1 STL/hello_user.stl STL
py3 $1 STL/hello_world.stl STL
