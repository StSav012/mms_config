# coding=utf-8


"""
using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

public static void PaintRowsNumber(DataGridView grid, DataGridViewRowPostPaintEventArgs e) {
    Rectangle bounds = new Rectangle(e.RowBounds.Location.X, e.RowBounds.Location.Y, grid.RowHeadersWidth - 4, e.RowBounds.Height);
    TextRenderer.DrawText(e.Graphics, (e.RowIndex + 1).ToString(), grid.RowHeadersDefaultCellStyle.Font, bounds, grid.RowHeadersDefaultCellStyle.ForeColor, TextFormatFlags.Right | TextFormatFlags.VerticalCenter);
}

public static void DrawBackgroundColor(PaintEventArgs e, Rectangle Area) {
    Graphics graphics = e.Graphics;
    Color lightSkyBlue = Color.LightSkyBlue;
    Color white = Color.White;
    Brush brush = new LinearGradientBrush(Area, lightSkyBlue, white, LinearGradientMode.Horizontal);
    graphics.FillRectangle(brush, Area);
}

public static void DrawBackgroundColor(Graphics g, Rectangle Area) {
    Color lightSkyBlue = Color.LightSkyBlue;
    Color white = Color.White;
    Brush brush = new LinearGradientBrush(Area, lightSkyBlue, white, LinearGradientMode.Horizontal);
    g.FillRectangle(brush, Area);
}

public static void DrawBackgroundColor(PaintEventArgs e, Rectangle Area, Color FColor, Color TColor, LinearGradientMode GraphicMode) {
    try {
        Rectangle rect = new Rectangle(0, 0, 3000, 1500);
        Graphics graphics = e.Graphics;
        Brush brush = new LinearGradientBrush(rect, FColor, TColor, GraphicMode);
        graphics.FillRectangle(brush, rect);
    } catch (SystemException) {}
}

public static void DrawBackgroundColor(Graphics g, Rectangle Area, Color FColor, Color TColor, LinearGradientMode GraphicMode) {
    Brush brush = new LinearGradientBrush(Area, FColor, TColor, GraphicMode);
    g.FillRectangle(brush, Area);
}

"""


def GetSystemDateTime() -> list[int]:
    from datetime import datetime

    now: datetime = datetime.now()
    return [
        now.year % 100,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
    ]


"""
public static void Memset(int[] buf, int val, int size) {
    for (int i = 0; i < size; i++) {
        buf[i] = val;
    }
}
"""


def DataEncryption(data: bytes | bytearray) -> bytearray:
    return bytearray(255 - (((num & 0xFF) >> 4) + ((num & 0xF) << 4)) for num in data)


"""
public static void DataDecryption(int[] Data) {
    int num = 0;
    for (int i = 0; i < Data.Length; i++) {
        num = Data[i];
        int num2 = ((num & 0xFF) >> 4) + ((num & 0xF) << 4);
        num2 = 255 - num2;
        Data[i] = num2;
    }
}

public static byte[] IntToByte(int[] data) {
    int num = data.Length;
    byte[] array = new byte[num];
    for (int i = 0; i < num; i++) {
        array[i] = (byte) data[i];
    }
    return array;
}

public static int[] ByteToInt(byte[] data) {
    int num = data.Length;
    int[] array = new int[num];
    for (int i = 0; i < num; i++) {
        array[i] = data[i];
    }
    return array;
}
"""
