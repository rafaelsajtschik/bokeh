import {LayoutDOM, LayoutDOMView} from "../layouts/layout_dom"
import {SizeHint, Layoutable} from "core/layout"
import {unsized, outer_size} from "core/dom"
import {Class} from "core/class"

export class DOMLayout extends Layoutable {

  constructor(readonly el: HTMLElement) {
    super()
  }

  size_hint(): SizeHint {
    let width: number

    const size = unsized(this.el, () => outer_size(this.el))

    if (this.sizing.width_policy == "fixed")
      width = this.sizing.width
    else
      width = this._clip_width(Math.ceil(size.width))

    let height: number
    if (this.sizing.height_policy == "fixed")
      height = this.sizing.height
    else
      height = this._clip_height(Math.ceil(size.height))

    return {width, height}
  }
}

export namespace WidgetView {
  export type Options = LayoutDOMView.Options & {model: Widget}
}

export abstract class WidgetView extends LayoutDOMView {
  model: Widget
  default_view: Class<WidgetView, [WidgetView.Options]>

  get child_models(): LayoutDOM[] {
    return []
  }

  _update_layout(): void {
    this.layout = new DOMLayout(this.el)
    this.layout.sizing = this.box_sizing()
  }
}

export namespace Widget {
  export interface Attrs extends LayoutDOM.Attrs {}

  export interface Props extends LayoutDOM.Props {}
}

export interface Widget extends Widget.Attrs {}

export abstract class Widget extends LayoutDOM {
  properties: Widget.Props

  constructor(attrs?: Partial<Widget.Attrs>) {
    super(attrs)
  }

  static initClass(): void {
    this.prototype.type = "Widget"
  }
}
Widget.initClass()
